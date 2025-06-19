### Function to display welcome message. Gives flexibility to use once or in other instances
def welcome_message():
    print("Welcome to the Daily Expense Tracker!")
    print("""
Menu:
1. Add a new expense
2. View all expenses
3. Calculate total and average expense
4. Clear all expenses
5. Exit""")

### Check if there is an empty list before processing menu options that use list contents
def empty_lst(lst):
    if len(lst) == 0:
        print("No expenses recorded yet.")
        return True
    else: return False

### Provides output of expenses in a ordered list format for option 2
def check_expenses(lst):
    print("Your expenses:")
    for index, expense in enumerate(lst):
        print(f'{index+1}. {expense}')

### Calculates the total for option 3
def calculate_total(lst):
    total = 0
    for i in lst:
        total += i
    print(f'Total expense: {total}')

### Calculates the average for option 3
def calculate_average(lst):
    total = 0
    for i in lst:
        total += i
    average = total / len(lst)
    print(f'Average expense: {average}')

### Main function which handles option processing
def menu_choice():
    expenses = []
    while True:
        choice = int(input())
        if choice in range(1,6):
            if choice == 1:
                expense = float(input())
                expenses.append(expense)
                print("Expense added successfully!")
            elif choice == 2:
                if not empty_lst(expenses):
                    check_expenses(expenses)
            elif choice == 3:
                if not empty_lst(expenses):
                    calculate_total(expenses)
                    calculate_average(expenses)
            elif choice == 4:
                expenses = []
                print("All expenses cleared.")
            elif choice == 5:
                print("Exiting the Daily Expense Tracker. Goodbye!")
                break
        else: print("Invalid choice. Please try again.")

welcome_message()
menu_choice()
