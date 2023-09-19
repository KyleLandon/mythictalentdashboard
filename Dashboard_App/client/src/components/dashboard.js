import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Dashboard() {
  const [creators, setCreators] = useState([]);

  useEffect(() => {
    loadCreators();
  }, []);
  
  const loadCreators = async () => {
    try {
      const res = await axios.get('http://localhost:3001/api/creators');
      setCreators(res.data);
      console.log('Creators data:', res.data); // Log the response data
    } catch (error) {
      console.error('Error loading creators:', error); // Log any errors
    }
  };

  return (
    <div>
      <h1>Creator Dashboard</h1>
      <table>
        <thead>
          <tr>
            <th>TM</th>
            <th>Creator</th>
            <th>Notes</th>
            <th>Exclusivity Status</th>
            <th>Agency %</th>
            <th>Tier</th>
            <th>Birthday</th>
            <th>Type</th>
            <th>Region</th>
            <th>Language</th>
            <th>Gender</th>
            <th>Total Reach</th>
            <th>Stream Link</th>
            <th>Followers</th>
            <th>CCV</th>
            <th>YouTube Link</th>
            <th>Subscribers</th>
            <th>Avg Views</th>
            <th>Shorts Avg Views</th>
            <th>Twitter Link</th>
            <th>Twitter Followers</th>
            <th>Instagram Link</th>
            <th>Instagram Followers</th>
            <th>TikTok Link</th>
            <th>TikTok Followers</th>
            <th>TikTok Avg Views</th>
            <th>TikTok Demos</th>
            <th>Twitch Demos</th>
            <th>YouTube Demos</th>
            <th>OS/Watch Time</th>
            <th>Device Demos</th>
            <th>Crypto</th>
            <th>Gambling</th>
            <th>NFTs</th>
            <th>1HR Stream Price</th>
            <th>2HR Stream Price</th>
            <th>30 Days Price</th>
            <th>YT Integration Price</th>
            <th>Dedicated Video Price</th>
            <th>Twitter Post Price</th>
            <th>IG Story Price</th>
            <th>IG Post Price</th>
            <th>TikTok Post Price</th>
          </tr>
        </thead>
        <tbody>
          {creators.map((creator, index) => (
            <tr key={index}>
              <td>{creator.TM}</td>
              <td>{creator.Creator}</td>
              <td>{creator.Notes}</td>
              <td>{creator.ExclusivityStatus}</td>
              <td>{creator.AgencyPercent}</td>
              <td>{creator.Tier}</td>
              <td>{new Date(creator.Birthday).toLocaleDateString()}</td>
              <td>{creator.Type}</td>
              <td>{creator.Region}</td>
              <td>{creator.Language}</td>
              <td>{creator.Gender}</td>
              <td>{creator.TotalReach}</td>
              <td>{creator.StreamLink}</td>
              <td>{creator.Followers}</td>
              <td>{creator.CCV}</td>
              <td>{creator.YouTubeLink}</td>
              <td>{creator.Subscribers}</td>
              <td>{creator.AvgViews}</td>
              <td>{creator.ShortsAvgViews}</td>
              <td>{creator.TwitterLink}</td>
              <td>{creator.TwitterFollowers}</td>
              <td>{creator.InstagramLink}</td>
              <td>{creator.InstagramFollowers}</td>
              <td>{creator.TikTokLink}</td>
              <td>{creator.TikTokFollowers}</td>
              <td>{creator.TikTokAvgViews}</td>
              <td>{creator.TikTokDemos}</td>
              <td>{creator.TwitchDemos}</td>
              <td>{creator.YouTubeDemos}</td>
              <td>{creator.OS_WatchTime}</td>
              <td>{creator.DeviceDemos}</td>
              <td>{creator.Crypto}</td>
              <td>{creator.Gambling}</td>
              <td>{creator.NFTs}</td>
              <td>{creator.OneHRStreamPrice}</td>
              <td>{creator.TwoHRStreamPrice}</td>
              <td>{creator.ThirtyDaysPrice}</td>
              <td>{creator.YTIntegrationPrice}</td>
              <td>{creator.DedicatedVideoPrice}</td>
              <td>{creator.TwitterPostPrice}</td>
              <td>{creator.IGStoryPrice}</td>
              <td>{creator.IGPostPrice}</td>
              <td>{creator.TikTokPostPrice}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Dashboard;
