from fastapi import FastAPI
import json

app = FastAPI()   # 👈 THIS LINE IS CRITICAL

@app.get("/workflows")
def get_workflows(platform: str = None):
    with open("workflows.json") as f:
        data = json.load(f)

    if platform:
        data = [d for d in data if d["platform"].lower() == platform.lower()]

    return data
