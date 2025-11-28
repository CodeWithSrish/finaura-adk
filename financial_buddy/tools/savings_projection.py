def project_savings(monthly_saving: float, years: int, interest_rate: float = 0.07):
    """
    Compound interest savings projection.
    """
    total_months = years * 12
    balance = 0

    for _ in range(total_months):
        balance += monthly_saving
        balance *= (1 + interest_rate / 12)

    return {"projected_savings": round(balance, 2)}
