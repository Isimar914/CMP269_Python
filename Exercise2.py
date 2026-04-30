class Payable:
    def process_payment(self, payment):
        pass
    def get_payment_status(self):
        pass

class PaymentMethod(Payable):
    total_transactions = 0

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def validate_account(self):
        pass

    def get_payment_status(self):
        return f"{self.account_holder}: ${self.balance}"

class CreditCard(PaymentMethod):
    def __init__(self, account_holder, balance, credit_limit):
        super().__init__(account_holder, balance)
        self.credit_limit = credit_limit

    def validate_account(self):
        return True

    def process_payment(self, amount):
        if amount > self.balance + self.credit_limit:
            return "Transaction Declined"
        else:
            self.balance -= amount
            PaymentMethod.total_transactions += 1
            return "Transaction Received"

class MealPlan(PaymentMethod):
    def __init__(self, account_holder, balance):
        super().__init__(account_holder, balance)

    def validate_account(self):
        return self.balance >= 0

    def process_payment(self, payment):
        if payment <= self.balance:
            self.balance -= payment
            PaymentMethod.total_transactions += 1
            return "Transaction Received"
        else:
            return "Transaction Declined"

def exercise_3_polymorphism():
    print("\n--- Payment System ---")

    cc = CreditCard("Alice", 100, 200)
    mp = MealPlan("Bob", 80)

    payments = [cc, mp]

    for payment in payments:
        result = payment.process_payment(50)
        print(result)
        print(payment.get_payment_status())

if __name__ == "__main__":
    payment1 = CreditCard("John Doe", 100, 200)
    payment2 = MealPlan("Jane Smith", 80)

    print(payment1.get_payment_status())
    print(payment2.get_payment_status())

    exercise_3_polymorphism()

    print("Total Transactions:", PaymentMethod.total_transactions)