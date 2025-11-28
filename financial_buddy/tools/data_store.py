import json
import os

DB_FILE = "user_data.json"

def save_transactions(transactions):
    """
    Save parsed transactions to file.
    """
    with open(DB_FILE, "w") as f:
        json.dump(transactions, f)

    return {"status": "saved"}

def get_transactions():
    """
    Load saved transactions.
    """
    if not os.path.exists(DB_FILE):
        return {"transactions": []}

    with open(DB_FILE, "r") as f:
        data = json.load(f)

    return {"transactions": data}
