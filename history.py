import json
import os

from config import HISTORY_FILE


def save_history(prompt):

    if not os.path.exists(HISTORY_FILE):

        with open(HISTORY_FILE, "w") as f:
            json.dump([], f)

    with open(HISTORY_FILE, "r") as f:
        history = json.load(f)

    history.append({
        "prompt": prompt
    })

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)