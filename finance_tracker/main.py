from finance_tracker.expense_manager import ExpenseManager
from finance_tracker.file_handler import save_expenses, load_expenses
from finance_tracker.reports import show_statistics
from finance_tracker.utils import validate_amount


def main():

    manager = ExpenseManager()

    # Load previous data
    saved_data = load_expenses()

    for item in saved_data:

        manager.add_expense(
            item["amount"],
            item["category"],
            item["description"]
        )

    print("=" * 60)
    print("         PERSONAL FINANCE TRACKER")
    print("=" * 60)

    while True:

        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. View Statistics")
        print("4. Save Expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            amount = input("Enter amount: ")

            if not validate_amount(amount):

                print("Invalid amount!")
                continue

            category = input("Enter category: ").title()
            description = input("Enter description: ")

            manager.add_expense(
                float(amount),
                category,
                description
            )

            print("Expense added successfully!")

        elif choice == "2":

            expenses = manager.get_all_expenses()

            print("\n========== ALL EXPENSES ==========")

            for expense in expenses:

                print(f"₹{expense.amount} | "
                      f"{expense.category} | "
                      f"{expense.description}")

        elif choice == "3":

            data = [expense.to_dict()
                    for expense in manager.get_all_expenses()]

            show_statistics(data)

        elif choice == "4":

            save_expenses(manager.get_all_expenses())

            print("Expenses saved successfully!")

        elif choice == "5":

            save_expenses(manager.get_all_expenses())

            print("\nThank you for using Finance Tracker!")
            break

        else:
            print("Invalid choice!")