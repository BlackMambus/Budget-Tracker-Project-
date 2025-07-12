import json
from datetime import datetime

class BudgetTracker:
    def __init__(self, filename="budget_data.json"):
        self.filename = filename
        self.transactions = []
        self.load_data()

    def add_transaction(self, amount, category, description):
        transaction = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.transactions.append(transaction)
        self.save_data()

    def get_balance(self):
        return sum(t["amount"] for t in self.transactions)

    def show_summary(self):
        print("\n📋 Transaction Summary:")
        for t in self.transactions:
            sign = "+" if t["amount"] > 0 else "-"
            print(f"{t['date']} | {t['category']} | {sign}₹{abs(t['amount'])} | {t['description']}")
        print(f"\n💼 Current Balance: ₹{self.get_balance():.2f}")

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.transactions, f, indent=4)

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                self.transactions = json.load(f)
        except FileNotFoundError:
            self.transactions = []

# Example usage
if __name__ == "__main__":
    tracker = BudgetTracker()

    while True:
        print("\n1. Add Income\n2. Add Expense\n3. Show Summary\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter income amount: ₹"))
            category = input("Enter income category: ")
            description = input("Enter description: ")
            tracker.add_transaction(amount, category, description)

        elif choice == "2":
            amount = float(input("Enter expense amount: ₹"))
            category = input("Enter expense category: ")
            description = input("Enter description: ")
            tracker.add_transaction(-amount, category, description)

        elif choice == "3":
            tracker.show_summary()

        elif choice == "4":
            print("Exiting Budget Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
