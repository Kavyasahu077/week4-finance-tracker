from finance_tracker.expense import Expense


class ExpenseManager:

    def __init__(self):

        self.expenses = []

    def add_expense(self, amount, category, description):

        expense = Expense(amount, category, description)

        self.expenses.append(expense)

    def get_all_expenses(self):

        return self.expenses