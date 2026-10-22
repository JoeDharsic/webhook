
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal

app = FastAPI()

# Temporary storage for practice only.
processed_events = set()
orders = {}


class OrderEvent(BaseModel):
    event_id: str
    event: Literal["order.created"]
    order_id: str
    amount: float


@app.get("/")
def home():
    return {"message": "Webhook server is running!"}


@app.post("/webhook")
def receive_webhook(payload: OrderEvent):
    # Check whether we have processed this event before.
    if payload.event_id in processed_events:
        return {
            "status": "duplicate",
            "message": "Event already processed",
        }

    # Simulate creating an order.
    orders[payload.order_id] = {
        "amount": payload.amount,
    }

    processed_events.add(payload.event_id)

    print("New order processed:", payload.order_id)

    return {
        "status": "success",
        "message": "Order processed",
        "order_id": payload.order_id,
    }
