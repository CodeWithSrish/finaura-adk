import csv
from typing import List, Dict

def parse_transactions(csv_text: str) -> List[Dict]:
    """
    Parse CSV transaction data into a structured list.
    """
    rows = []
    reader = csv.DictReader(csv_text.splitlines())
    for row in reader:
        rows.append({
            "date": row.get("date"),
            "description": row.get("description"),
            "amount": float(row.get("amount", 0)),
            "category": row.get("category", "uncategorized")
        })
    return rows
