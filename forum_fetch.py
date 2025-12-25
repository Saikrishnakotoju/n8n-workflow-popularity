import requests
import json

url = "https://community.n8n.io/latest.json"
data = requests.get(url).json()

forum_workflows = []

for topic in data["topic_list"]["topics"][:10]:
    forum_workflows.append({
        "workflow": topic["title"],
        "platform": "Forum",
        "popularity_metrics": {
            "replies": topic["reply_count"],
            "likes": topic["like_count"],
            "views": topic["views"]
        },
        "country": "Global"
    })

# Load existing YouTube data
with open("workflows.json", "r") as f:
    existing = json.load(f)

# Combine and save
with open("workflows.json", "w") as f:
    json.dump(existing + forum_workflows, f, indent=2)

print("Added forum workflows")
