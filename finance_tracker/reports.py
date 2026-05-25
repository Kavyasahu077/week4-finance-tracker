def show_statistics(expenses):

    if not expenses:
        print("No expenses found!")
        return

    total = sum(expense["amount"] for expense in expenses)

    print("\n========== EXPENSE REPORT ==========")
    print(f"Total Expenses: ₹{total}")

    categories = {}

    for expense in expenses:

        category = expense["category"]

        categories[category] = categories.get(category, 0) + expense["amount"]

    print("\nCategory Breakdown:")

    for category, amount in categories.items():

        print(f"{category}: ₹{amount}")