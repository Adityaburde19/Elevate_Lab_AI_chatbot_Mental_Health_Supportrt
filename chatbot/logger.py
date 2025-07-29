import datetime
import os
import csv

LOG_DIR = "chat_logs"

def log_session(session_id: str, user_input: str, bot_response: str):
    os.makedirs(LOG_DIR, exist_ok=True)
    filename = os.path.join(LOG_DIR, f"{session_id}.csv")

    with open(filename, mode="a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.datetime.now().isoformat(),
            session_id,
            user_input,
            bot_response
        ])
