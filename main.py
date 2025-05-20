from fastapi import FastAPI, Request
from bitrix import send_lead_to_bitrix

app = FastAPI()

@app.post("/webhook")
async def meta_webhook(request: Request):
    body = await request.json()
    
    # Розбір події
    entry = body.get("entry", [])[0]
    changes = entry.get("changes", [])[0]
    leadgen_id = changes["value"]["leadgen_id"]
    form_id = changes["value"]["form_id"]

    # Тут можна звернутись до Meta Graph API, щоб отримати повні дані
    # але для простоти припустимо, що їх вже отримано
    # ❗️На практиці треба підтягнути lead data через токен

    lead_data = {
        "first_name": "Test",
        "phone_number": "+380501112233",
        "email": "test@example.com",
        "utm_source": "facebook",
        "utm_medium": "cpc",
        "utm_campaign": "test_campaign",
        "utm_term": "test_term",
        "utm_content": "ad1",
    }

    result = await send_lead_to_bitrix(lead_data)
    return {"status": "received", "bitrix_response": result}
