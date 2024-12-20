class BankSystem:
    def __init__(self, bank_name, account_balance):
        self.bank_name = bank_name
        self.account_balance = account_balance

    def validate_transaction(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds.")
            return False
        return True

    def process_transaction(self, amount):
        self.account_balance -= amount
        print(f"Transaction successful! Remaining balance: ${self.account_balance:.2f}")


class ATMCard:
    def __init__(self, card_number, bank_name):
        self.card_number = card_number
        self.bank_name = bank_name


class ATMMachine:
    def __init__(self, bank_system):
        self.bank_system = bank_system

    def validate_pin(self, entered_pin, correct_pin):
        if entered_pin == correct_pin:
            return True
        print("Invalid PIN. Please try again.")
        return False

    def process_transaction(self, option, amount):
        if option == 1:
            if self.bank_system.validate_transaction(amount):
                self.bank_system.process_transaction(amount)
                print("Please collect your cash.")
        elif option == 2:
            print(f"Your account balance is: ${self.bank_system.account_balance:.2f}")
        else:
            print("Invalid option selected.")


class Customer:
    def __init__(self, name, atm_card):
        self.name = name
        self.atm_card = atm_card

    def use_atm(self, atm, correct_pin):
        print(f"Welcome, {self.name}!")
        entered_pin = int(input("Please enter your PIN: "))

        if atm.validate_pin(entered_pin, correct_pin):
            print("Select Transaction: (1) Withdrawal (2) Balance Inquiry")
            option = int(input("Enter your choice: "))

            if option == 1:
                amount = float(input("Enter amount to withdraw: "))
                atm.process_transaction(option, amount)
            elif option == 2:
                atm.process_transaction(option, 0)
            else:
                print("Invalid option.")



bank = BankSystem("Example Bank", 5000.00)
card = ATMCard(12345678, "Example Bank")
customer = Customer("Khalid Elabd", card)
atm = ATMMachine(bank)

customer.use_atm(atm, 1234)
