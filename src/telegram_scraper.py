import os
import pandas as pd
from telethon.sync import TelegramClient

API_ID   = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")

def scrape_channel(channel: str, limit: int = 500) -> pd.DataFrame:
    with TelegramClient("ethioMart", API_ID, API_HASH) as client:
        msgs = list(client.iter_messages(channel, limit=limit))
    return pd.DataFrame([{
        "date":    m.date,
        "sender":  m.sender_id,
        "raw":     m.message,
        "views":   m.views,
        "channel": channel
    } for m in msgs])
