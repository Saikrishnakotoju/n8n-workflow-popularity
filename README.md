# n8n Workflow Popularity System

This project identifies popular **n8n workflows** across multiple platforms using real engagement data and exposes the results through a REST API.

The goal is to surface workflows that are actively used and discussed, supported by clear and measurable popularity signals.

---

## 📌 What This Project Does

- Collects real data from:
  - **YouTube** (n8n workflow videos)
  - **n8n Community Forum** (Discourse)
- Measures popularity using:
  - Views, likes, and comment counts
  - Engagement ratios (likes/views, comments/views)
- Stores results in a structured JSON dataset
- Exposes the data via a **REST API** using FastAPI
- Includes a **cron-ready script** to refresh data automatically

---

## 🔗 Data Sources

### YouTube Data API v3
Used to fetch:
- Video view counts
- Like counts
- Comment counts

### n8n Community Forum (Discourse API)
Used to fetch:
- Topic reply counts
- Likes
- View counts

---

## 📊 Popularity Metrics

Each workflow includes:
- View count
- Like count
- Comment count
- Engagement ratios:
  - `like_to_view_ratio`
  - `comment_to_view_ratio`

These metrics help identify workflows with strong community interest and interaction.

---

## 🏗 Project Structure

n8n-workflow-popularity/
│
├── youtube_fetch.py # Fetches YouTube workflow data
├── forum_fetch.py # Fetches n8n forum data
├── workflows.json # Combined dataset
├── app.py # FastAPI REST API
├── cron_job.py # Automation script
├── requirements.txt # Project dependencies
└── README.md

yaml
Copy code

---

## 🚀 How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
2️⃣ Fetch workflow data
bash
Copy code
python youtube_fetch.py
python forum_fetch.py
3️⃣ Start the API server
bash
Copy code
python -m uvicorn app:app --reload
Open in browser:

arduino
Copy code
http://127.0.0.1:8000/workflows
⏰ Automation (Cron-Ready)
The cron_job.py script refreshes workflow data automatically.

Example cron schedule:

bash
Copy code
0 2 * * * python cron_job.py
📈 Scalability & Future Enhancements
Easy integration of additional platforms (e.g., Google Trends)

Support for larger datasets

Migration from JSON storage to a database if required


Hi Team,  
>  
> I’ve completed the technical assignment and shared the GitHub repository below.  
>  
> The project implements a scalable prototype that identifies popular n8n workflows using real engagement data from YouTube and the n8n community forum. It computes clear popularity metrics, exposes the results via a REST API, and includes a cron-ready script for automated updates.  
>  
> The architecture is designed to be easily extended with additional data sources such as Google Trends.  
>  
> Looking forward to your feedback.  
>  
> Thanks,  
> **Sai Krishna**
