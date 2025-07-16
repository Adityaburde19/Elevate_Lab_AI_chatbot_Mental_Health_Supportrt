import datetime

def log_session(user_input, bot_response):
    with open("chat_logs.txt", "a") as f:
        f.write(f"{datetime.datetime.now()} - User: {user_input}\n")
        f.write(f"{datetime.datetime.now()} - Bot: {bot_response}\n\n")
