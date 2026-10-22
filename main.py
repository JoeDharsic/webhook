
from fastapi import FastAPI, Request, HTTPException

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Webhook server is running!"}


@app.post("/webhook")
async def receive_webhook(request: Request):
    # GitHub identifies the event using this header.
    event_type = request.headers.get("X-GitHub-Event", "unknown")

    try:
        payload = await request.json()
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid JSON payload",
        )

    if event_type == "push":
        repository = payload.get("repository", {})
        commits = payload.get("commits", [])

        print(
            f"Push received for {repository.get('full_name')}"
        )
        print(f"Number of commits: {len(commits)}")

        return {
            "status": "success",
            "event": "push",
            "repository": repository.get("full_name"),
            "commit_count": len(commits),
        }

    if event_type == "ping":
        return {"status": "success", "event": "ping"}

    return {
        "status": "ignored",
        "event": event_type,
    }
