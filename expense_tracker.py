import sys
import json
import os
from datetime import datetime
import argparse

EXPENSE_FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(EXPENSE_FILE):
        return []
    with open(EXPENSE_FILE, "r") as f:
        return json.load(f)

def save_expenses(expenses):
    with open(EXPENSE_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(description, amount):
    expenses = load_expenses()
    expense_id = len(expenses) + 1
    expense = {
        "id": expense_id,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "amount": float(amount)
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {expense_id})")

def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    print(f"{'ID':<5} {'Date':<12} {'Description':<20} {'Amount':<10}")
    for expense in expenses:
        print(f"{expense['id']:<5} {expense['date']:<12} {expense['description']:<20} ${expense['amount']:<10.2f}")

def delete_expense(expense_id):
    expenses = load_expenses()
    updated_expenses = [expense for expense in expenses if expense["id"] != int(expense_id)]
    if len(expenses) == len(updated_expenses):
        print(f"Expense with ID {expense_id} not found.")
        return
    save_expenses(updated_expenses)
    print(f"Expense deleted successfully (ID: {expense_id})")

def update_expense(expense_id, description, amount):
    expenses = load_expenses()
    for expense in expenses:
        if expense["id"] == int(expense_id):
            expense["description"] = description
            expense["amount"] = float(amount)
            expense["date"] = datetime.now().strftime("%Y-%m-%d")
            save_expenses(expenses)
            print(f"Expense updated successfully (ID: {expense_id})")
            return
    print(f"Expense with ID {expense_id} not found.")

def summary(month=None):
    expenses = load_expenses()
    if month:
        current_year = datetime.now().year
        month_expenses = [expense for expense in expenses if datetime.strptime(expense["date"], "%Y-%m-%d").month == int(month) and datetime.strptime(expense["date"], "%Y-%m-%d").year == current_year]
        total = sum(expense["amount"] for expense in month_expenses)
        print(f"Total expenses for {datetime.strptime(str(month), '%m').strftime('%B')}: ${total:.2f}")
    else:
        total = sum(expense["amount"] for expense in expenses)
        print(f"Total expenses: ${total:.2f}")

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add expense command
    parser_add = subparsers.add_parser("add", help="Add a new expense")
    parser_add.add_argument("--description", required=True, help="Description of the expense")
    parser_add.add_argument("--amount", required=True, type=float, help="Amount of the expense")

    # List expenses command
    parser_list = subparsers.add_parser("list", help="List all expenses")

    # Delete expense command
    parser_delete = subparsers.add_parser("delete", help="Delete an expense")
    parser_delete.add_argument("--id", required=True, help="ID of the expense to delete")

    # Update expense command
    parser_update = subparsers.add_parser("update", help="Update an expense")
    parser_update.add_argument("--id", required=True, help="ID of the expense to update")
    parser_update.add_argument("--description", required=True, help="New description of the expense")
    parser_update.add_argument("--amount", required=True, type=float, help="New amount of the expense")

    # Summary command
    parser_summary = subparsers.add_parser("summary", help="Show a summary of expenses")
    parser_summary.add_argument("--month", type=int, help="Month (1-12) to filter the expenses summary")

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount)
    elif args.command == "list":
        list_expenses()
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "update":
        update_expense(args.id, args.description, args.amount)
    elif args.command == "summary":
        summary(args.month)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
