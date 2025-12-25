"""
Cron Job Script for n8n Workflow Popularity System

This script refreshes workflow popularity data by
fetching the latest data from YouTube and the n8n forum.

It is intended to be run daily or weekly using cron or
any task scheduler.
"""

import os

print("Starting cron job...")

# Run YouTube data fetch
os.system("python youtube_fetch.py")

# Run Forum data fetch
os.system("python forum_fetch.py")

print("Cron job completed successfully.")
