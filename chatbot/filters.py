import re

# Improved safety keywords
keywords = [
    "suicide", "kill myself", "end it all", "die", "worthless", "hopeless",
    "cut", "jump off", "no way out", "can't go on", "self harm"
]

def is_offensive(text: str) -> bool:
    clean = re.sub(r'[^\w\s]', '', text.lower())
    return any(k in clean for k in keywords)

def flag_keywords(text: str):
    # Return matched harmful phrases for diagnostics
    clean = re.sub(r'[^\w\s]', '', text.lower())
    return [k for k in keywords if k in clean]
