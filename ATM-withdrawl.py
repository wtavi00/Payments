print("Welcome to the ATM Withdrawal System!")

def get_valid_amount(prompt):
    while True:
        try:
            amount = int(input(prompt))
            if amount > 0:
                return amount
            else:
                print("Invalid input. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

account_balance = get_valid_amount("Enter the account balance: ")

while True:
    withdrawal_amount = get_valid_amount("Enter the amount you want to withdraw: ")

    if withdrawal_amount > account_balance:
        print("Insufficient balance. Try again.")
    else:
        remaining_amount = account_balance - withdrawal_amount
        print("Withdrawal Successful!")
        print("Remaining Balance: $", remaining_amount)
        break  
