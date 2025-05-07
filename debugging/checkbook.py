import sys

def clear_screen():
    """
    Clear the console screen for better readability of the menu.
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

class Checkbook:
    """
    A simple checkbook class to manage deposits, withdrawals, and balance inquiries.
    """
    def __init__(self):
        """
        Initialize the checkbook with a zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a positive amount to the checkbook.

        Parameters:
            amount (float): The amount to be deposited; must be positive.

        Returns:
            None
        """
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        print(f"Current Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraw a positive amount from the checkbook if funds are sufficient.

        Parameters:
            amount (float): The amount to withdraw; must be positive and <= balance.

        Returns:
            None
        """
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")
            print(f"Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        """
        Print the current balance.

        Returns:
            None
        """
        print(f"Current Balance: ${self.balance:.2f}")


def main():
    """
    Main loop to interact with the user for banking actions.
    Supports deposit, withdraw, balance inquiry, and exit.
    Prevents crashing on invalid (non-numeric) inputs.
    """
    cb = Checkbook()
    actions = {'deposit', 'withdraw', 'balance', 'exit'}

    while True:
        clear_screen()
        print("Available actions: deposit, withdraw, balance, exit")
        action = input("What would you like to do? ").strip().lower()

        if action not in actions:
            print("Invalid command. Please try again.")
            input("Press Enter to continue...")
            continue

        if action == 'exit':
            print("Goodbye!")
            break

        # For deposit and withdraw, prompt for amount safely
        if action in ('deposit', 'withdraw'):
            try:
                raw = input(f"Enter the amount to {action}: $")
                amount = float(raw)
            except ValueError:
                print("Error: Please enter a valid numeric amount.")
                input("Press Enter to continue...")
                continue

            if action == 'deposit':
                cb.deposit(amount)
            else:
                cb.withdraw(amount)

        elif action == 'balance':
            cb.get_balance()

        input("Press Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nSession interrupted. Exiting.")
        sys.exit(0)