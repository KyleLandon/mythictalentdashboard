import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
# webscrape google account: mythic-talent@mythic-talent-webscrape.iam.gserviceaccount.com

# Web Scraping Function
def get_viewership(creator_name):
    url = f"https://sullygnome.com/channel/{creator_name}/30"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    
    # Check the response status
    if response.status_code != 200:
        print(f"Unexpected status code for {creator_name}: {response.status_code}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    
    viewership_element = soup.select_one("body > div.RightContent > div.MainContent > div.InfoStatPanelContainerTop > div > div.InfoStatPanelWrapper.InfoStatPanelSpacerLeft > div > div > div.InfoStatPanelTL > div")
    
    if viewership_element:
        viewership = viewership_element.text.strip()
        if viewership == "395,717,372":  # Special case
            print(f"Channel {creator_name} not found.")
            return None
        print(f"Viewership for {creator_name}: {viewership}")
        return viewership
    else:
        print(f"Failed to fetch viewership for {creator_name}.")
        return None



# Grab list of creators from Google Sheet
def fetch_creators_from_gsheet(workbook_name, sheet_name, col_index):
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        client = gspread.authorize(creds)

        sheet = client.open(workbook_name).worksheet(sheet_name)
        creators_list = sheet.col_values(col_index)[1:]  # Exclude the first row
        print(f"Fetched {len(creators_list)} creators from Google Sheet.")
        return creators_list
    except Exception as e:
        print(f"Error encountered while fetching creators from Google Sheet: {e}")
        return []


# Update the Google Sheet with Webscrapped Data
def update_google_sheet(workbook_name, sheet_name, creator_name, viewership, creator_col_index, viewership_col_index):
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        client = gspread.authorize(creds)

        sheet = client.open(workbook_name).worksheet(sheet_name)

        all_creators = sheet.col_values(creator_col_index)
        if creator_name in all_creators:
            row_number = all_creators.index(creator_name) + 1
            sheet.update_cell(row_number, viewership_col_index, viewership)
            print(f"Updated viewership for {creator_name} in row {row_number}, column {viewership_col_index} of {sheet_name} in {workbook_name}.")
    except Exception as e:
        print(f"Error encountered while updating Google Sheet for {creator_name}: {e}")



# Main Program Execution
if __name__ == "__main__":
    print("Starting the scraping process...")
    
    creators1 = fetch_creators_from_gsheet("Kyles Copy Internal", "Overview", 2)
    creators2 = fetch_creators_from_gsheet("Kyles Copy External", "Talent Roster Overview", 1)  # Different column for creators

    all_creators = creators1 + creators2  # Combine lists if needed, or process them separately
    
    for creator in creators1:
        viewership = get_viewership(creator)
        if viewership is not None:
            update_google_sheet("Kyles Copy Internal", "Sheet1", creator, viewership, 2, 15) 
            # First number is the creator column, Last number is the column of CCV
        
        time.sleep(10)

    for creator in creators2:
        viewership = get_viewership(creator)
        if viewership is not None:
            update_google_sheet("Kyles Copy External", "Sheet1", creator, viewership, 1, 10)  
            # First number is the creator column, Last number is the column of CCV
        time.sleep(10)

    print("Scraping process completed!")















