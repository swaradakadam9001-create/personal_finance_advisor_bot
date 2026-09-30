from collections import defaultdict

def analyze(incomes, expenses):
    total_income = sum(x.amount for x in incomes)
    total_expense = sum(x.amount for x in expenses)
    savings = total_income - total_expense
    categories = defaultdict(float)
    for e in expenses:
        categories[e.category] += e.amount

    overspending = []
    for cat, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        share = (amount / total_income * 100) if total_income else 0
        if share >= 20:
            overspending.append((cat, amount, round(share, 1)))

    suggestions = []
    if total_income <= 0:
        suggestions.append("Add your monthly income to generate a personalized budget.")
    else:
        if total_expense > total_income:
            suggestions.append("Your expenses are above income. Reduce non-essential spending first.")
        if categories.get("Entertainment", 0) > total_income * 0.10:
            suggestions.append("Consider setting an entertainment limit near 10% of income.")
        if categories.get("Food", 0) > total_income * 0.15:
            suggestions.append("Review food spending and plan weekly meals to reduce avoidable costs.")
        if savings < total_income * 0.20:
            suggestions.append("Try to build savings toward at least 20% of monthly income.")
        else:
            suggestions.append("Your current savings level provides a useful base for future goals.")
        suggestions.append("Use a weekly spending check-in to catch budget drift early.")

    return {
        "income": round(total_income, 2),
        "expenses": round(total_expense, 2),
        "savings": round(savings, 2),
        "categories": dict(categories),
        "overspending": overspending,
        "suggestions": suggestions,
    }
