import os
from dotenv import load_dotenv
import httpx

load_dotenv()
BITRIX_WEBHOOK = os.getenv("BITRIX_WEBHOOK")

async def send_lead_to_bitrix(data: dict):
    payload = {
        "fields": {
            "TITLE": "Лід з Meta Lead Ads",
            "NAME": data.get("first_name", ""),
            "PHONE": [{"VALUE": data.get("phone_number", ""), "VALUE_TYPE": "WORK"}],
            "EMAIL": [{"VALUE": data.get("email", ""), "VALUE_TYPE": "WORK"}],
            "UTM_SOURCE": data.get("utm_source"),
            "UTM_MEDIUM": data.get("utm_medium"),
            "UTM_CAMPAIGN": data.get("utm_campaign"),
            "UTM_TERM": data.get("utm_term"),
            "UTM_CONTENT": data.get("utm_content"),
        }
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(BITRIX_WEBHOOK, json=payload)
        return response.json()
