import json

FILE_PATH = "data/expenses.json"


def save_expenses(expenses):

    data = [expense.to_dict() for expense in expenses]

    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)


def load_expenses():

    try:

        with open(FILE_PATH, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []