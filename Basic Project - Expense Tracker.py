import json
import os

def load_expenses():
    if os.path.exists("expenses.json"):
        try:
            with open("expenses.json", "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            print("Error loading expenses from file.")
            return []
    return []

def save_expenses(expenses, filename="expenses.json"):
    try:
        with open(filename, "w") as file:
            json.dump(expenses, file, indent=4)
        print("Data saved successfully!")
    except IOError:
        print("Error saving data to file.")

def add_expenses(expenses):
    title = input("Enter the title of the expense: ").strip()
    while True:
        try:
            amount = float(input("Enter the amount of the expense: ").strip())
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.") 
    category = input("Enter the category of the expense: ").strip()
    date = input("Enter date (DD-MM-YYYY): ").strip()

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
        
    print ("\n---Expenses: ---")
    for expense in expenses:
        print(f"Title: {expense['title']}, Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}")

def summary_expenses(expenses):  
    if not expenses:
        print("No expenses recorded.")
        return
    
    total_expense = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal Expenses: {total_expense}")
    total_count= len(expenses)
    print(f"Total number of expenses: {total_count}")
    average_expense = total_expense / total_count
    print(f"Average expense amount: {average_expense:.2f}")
    highest_spending = max(expense['amount'] for expense in expenses)
    print(f"Highest spending amount: {highest_spending}")

def main() :
    print ("Welcome Rey's Expense Tracker!")
    expenses = load_expenses()

    while True :
        print("\nPlease select an option:")
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            summary_expenses(expenses)
        elif choice == "4": 
            save_expenses(expenses)
            print("Thank you for using Rey's Expense Tracker!")
            break
        else :
            print("Invalid choice. try again.")

main()