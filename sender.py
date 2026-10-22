
import json
from urllib.request import Request, urlopen

WEBHOOK_URL = "https://webhook.site/dbbe5ec9-0589-4e58-85b7-6c2f1e61e5d6"

payload = {
    "event": "order.created",
    "order_id": "ORD-101",
    "table_number": 5,
    "amount": 850,
}

data = json.dumps(payload).encode("utf-8")

request = Request(
    WEBHOOK_URL,
    data=data,
    headers={"Content-Type": "application/json"},
    method="POST",
)

with urlopen(request, timeout=15) as response:
    print("Status:", response.status)
    print("Response:", response.read().decode("utf-8"))

print("Webhook sent successfully!")
