from typing import List, Dict

def summarize_transactions(transactions: List[Dict]) -> Dict:
    """
    Summarize spending across categories.
    """
    summary = {}
    for tx in transactions:
        cat = tx.get("category", "uncategorized")
        amt = tx.get("amount", 0)
        summary[cat] = summary.get(cat, 0) + amt

    return summary
