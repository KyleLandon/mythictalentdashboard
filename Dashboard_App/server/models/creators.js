const mongoose = require('mongoose');

const creatorsSchema = new mongoose.Schema({
    TM: String,
    Creator: String,
    Notes: String,
    ExclusivityStatus: String,
    AgencyPercent: String,  // Changed from Number to String to match your data
    Tier: String,
    Birthday: String,  // Changed from Date to String to match your data
    Type: String,
    Region: String,
    Language: String,
    Gender: String,
    TotalReach: String,  // Changed from Number to String to match your data
    StreamLink: String,
    Followers: String,
    CCV: String,
    YouTubeLink: String,
    Subscribers: String,
    AvgViews: String,
    ShortsAvgViews: String,
    TwitterLink: String,
    TwitterFollowers: String,
    InstagramLink: String,
    InstagramFollowers: String,
    TikTokLink: String,
    TikTokFollowers: String,
    TikTokAvgViews: String,
    TikTokDemos: String,
    TwitchDemos: String,
    YouTubeDemos: String,
    OS_WatchTime: String,
    DeviceDemos: String,
    Crypto: String,
    Gambling: String,
    NFTs: String,
    OneHRStreamPrice: String,
    TwoHRStreamPrice: String,
    ThirtyDaysPrice: String,
    YTIntegrationPrice: String,
    DedicatedVideoPrice: String,
    TwitterPostPrice: String,
    IGStoryPrice: String,
    IGPostPrice: String,
    TikTokPostPrice: String
});

module.exports = mongoose.model('Creator', creatorsSchema);
