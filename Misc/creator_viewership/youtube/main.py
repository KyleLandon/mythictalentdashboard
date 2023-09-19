import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials

def fetch_creators_from_gsheet():
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        client = gspread.authorize(creds)

        sheet = client.open("WEBSCRAPE PRACTICE").sheet1
        creators_list = sheet.col_values(2)[1:]  # Assuming channel IDs (creators) are in the second column and excluding the header
        print(f"Fetched {len(creators_list)} creators from Google Sheet.")
        return creators_list
    except Exception as e:
        print(f"Error encountered while fetching creators from Google Sheet: {e}")
        return []

def get_average_views(creator_name, api_key):
    base_url = "https://www.googleapis.com/youtube/v3"
    max_results = 50

    try:
        response = requests.get(f"{base_url}/search?key={api_key}&channelId={creator_name}&part=id&order=date&maxResults={max_results}&type=video")
        response_data = response.json()

        # Check for API errors
        if 'error' in response_data:
            print(f"API Error for creator {creator_name}: {response_data['error']['message']}")
            return None

        video_ids = [item['id']['videoId'] for item in response_data.get('items', [])]

        if not video_ids:
            print(f"No videos found for the creator: {creator_name}")
            return None

        video_stats_response = requests.get(f"{base_url}/videos?key={api_key}&id={','.join(video_ids)}&part=statistics")
        video_stats_data = video_stats_response.json()

        # Check for API errors again
        if 'error' in video_stats_data:
            print(f"API Error when fetching video stats for creator {creator_name}: {video_stats_data['error']['message']}")
            return None

        video_stats = video_stats_data.get('items', [])

        total_views = sum(int(video['statistics']['viewCount']) for video in video_stats)
        average_views = total_views / len(video_stats)

        return average_views

    except Exception as e:
        print(f"Error encountered while fetching average views for creator {creator_name}: {e}")
        return None


def update_google_sheet(creator_name, average_views):
    try:
        scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
        client = gspread.authorize(creds)

        sheet = client.open("WEBSCRAPE PRACTICE").sheet1

        all_creators = sheet.col_values(2)
        if creator_name in all_creators:
            row_number = all_creators.index(creator_name) + 1
            sheet.update_cell(row_number, 18, average_views)  # Assuming column 18 (R) is where you want to store the average views
            print(f"Updated average views for {creator_name} in row {row_number}.")
        else:
            print(f"Creator {creator_name} not found in the sheet.")
    except Exception as e:
        print(f"Error encountered while updating Google Sheet for {creator_name}: {e}")

if __name__ == "__main__":
    API_KEY = "AIzaSyCjqLRRNMV4Svl8ljRS9ERKuwTRoOiVfHM"
    creators = fetch_creators_from_gsheet()

    for creator_name in creators:
        average = get_average_views(creator_name, API_KEY)
        if average:
            print(f"Average views for creator {creator_name}: {average:.2f}")
            update_google_sheet(creator_name, average)
        else:
            print(f"Failed to fetch average views for creator {creator_name}")
