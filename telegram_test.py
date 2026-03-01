"""
Simple Telegram test — run this first to confirm bot works on GitHub Actions
"""
import os
import requests

TOKEN   = os.environ.get("TELEGRAM_TOKEN", "7753587413:AAHWLS-qZ7aVxMCycHiT8yhaUcEHNlRg_hU")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "8129647943")

print(f"Token  : {TOKEN[:20]}...")
print(f"Chat ID: {CHAT_ID}")

msg = (
    "✅ GitHub Actions Test SUCCESS\n"
    "Your BankNifty bot is working!\n"
    "You will now get trade signals automatically."
)

try:
    url  = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    resp = requests.post(url, data={
        "chat_id"   : CHAT_ID,
        "text"      : msg,
        "parse_mode": "HTML"
    }, timeout=15)

    data = resp.json()
    print(f"Response: {data}")

    if data.get("ok"):
        print("SUCCESS — message sent to Telegram!")
    else:
        print(f"FAILED — {data.get('description')}")
        print("Check token and chat ID are correct")

except Exception as e:
    print(f"ERROR: {e}")
