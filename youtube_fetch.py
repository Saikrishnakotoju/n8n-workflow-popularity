import requests
import json

API_KEY = "AIzaSyDU3mh3GPBcDQwTB2c7laSN1Mzr4McsshU"

# 1. Search for n8n workflow videos
search_url = "https://www.googleapis.com/youtube/v3/search"
search_params = {
    "part": "snippet",
    "q": "n8n workflow",
    "type": "video",
    "maxResults": 10,
    "key": API_KEY
}

search_response = requests.get(search_url, params=search_params).json()

video_ids = []
titles = {}

for item in search_response["items"]:
    video_id = item["id"]["videoId"]
    title = item["snippet"]["title"]
    video_ids.append(video_id)
    titles[video_id] = title

# 2. Get statistics for those videos
stats_url = "https://www.googleapis.com/youtube/v3/videos"
stats_params = {
    "part": "statistics",
    "id": ",".join(video_ids),
    "key": API_KEY
}

stats_response = requests.get(stats_url, params=stats_params).json()

workflows = []

for item in stats_response["items"]:
    stats = item["statistics"]

    views = int(stats.get("viewCount", 0))
    likes = int(stats.get("likeCount", 0))
    comments = int(stats.get("commentCount", 0))

    if views == 0:
        continue

    workflows.append({
        "workflow": titles[item["id"]],
        "platform": "YouTube",
        "popularity_metrics": {
            "views": views,
            "likes": likes,
            "comments": comments,
            "like_to_view_ratio": round(likes / views, 4),
            "comment_to_view_ratio": round(comments / views, 4)
        },
        "country": "US"
    })

# 3. Save to JSON file
with open("workflows.json", "w") as f:
    json.dump(workflows, f, indent=2)

print("Saved", len(workflows), "YouTube workflows")
