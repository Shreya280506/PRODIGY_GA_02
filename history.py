import json
import os

from config import HISTORY_FILE


def save_history(prompt):

    history_dir = os.path.dirname(HISTORY_FILE)

    if history_dir:
        os.makedirs(history_dir, exist_ok=True)

    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump([], f)

    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        history = json.load(f)

    history.append({
        "prompt": prompt
    })

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4)