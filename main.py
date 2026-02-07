from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

API_KEY = "GUVI123"


# -------- request models --------

class MessageObj(BaseModel):
    sender: str
    text: str
    timestamp: int


class Metadata(BaseModel):
    channel: Optional[str] = None
    language: Optional[str] = None
    locale: Optional[str] = None


class HoneypotRequest(BaseModel):
    sessionId: str
    message: MessageObj
    conversationHistory: List[dict]
    metadata: Metadata


# -------- endpoint --------

@app.post("/honeypot")
def analyze_message(
    data: HoneypotRequest,
    x_api_key: str = Header(None)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    text = data.message.text.lower()

    scam_words = ["bank", "blocked", "click", "urgent", "otp", "verify"]
    found = [w for w in scam_words if w in text]

    is_scam = len(found) > 0

    if is_scam:
        reply = "⚠️ Potential scam detected. Do not click links or share OTP."
    else:
        reply = "Message looks safe."

    return {
        "status": "success",
        "reply": reply
    }