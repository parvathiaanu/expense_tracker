import json
expenses_file = "expenses.json"
def loadExpenses():
    try:
        with open(expenses_file, 'r') as file:
            expenses_data = json.load(file)
        return expenses_data
    except FileNotFoundError:
        return []

def saveExpenses():
    with open(expenses_file, 'w') as file:
        json.dump(expenses, file)

def addExpense(amount, category):  # Modified to accept parameters
    expense = {'amount': amount, 'category': category}
    expenses.append(expense)

def removeExpense():
    while True:
        listExpenses()
        print("What expense would you like to remove?")
        try:
            expenseToRemove = int(input("> "))
            if 0 <= expenseToRemove < len(expenses):
                del expenses[expenseToRemove]
                print("Expense removed successfully.")
                break
            else:
                print("Invalid index. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")

def printMenu():
    print("\nPlease choose from one of the following options...")
    print("1. Add a New Expense")
    print("2. Remove an Expense")
    print("3. List All Expenses")
    print("4. Exit")

def listExpenses():
    print("\nHere is a list of your expenses...")
    print("------------------------------------")
    counter = 0
    for expense in expenses:
        print("#", counter, " - ", expense['amount'], " - ", expense['category'])
        counter += 1
    print("\n\n")

expenses = loadExpenses()

if __name__ == "__main__":
    while True:
        printMenu()
        optionSelected = input("> ")

        if optionSelected == "1":
            print("How much was this expense?")
            amountToAdd = input("> ")
            print("What category was this expense?")
            category = input("> ")
            addExpense(amountToAdd, category)
            saveExpenses()  # Save after adding an expense
        elif optionSelected == "2":
            removeExpense()
            saveExpenses()  # Save after removing an expense
        elif optionSelected == "3":
            listExpenses()
        elif optionSelected == "4":
            print("Exiting the program. Goodbye!")
            saveExpenses()  # Save before exiting
            break
        else:
            print("Invalid input. Please try again.")
