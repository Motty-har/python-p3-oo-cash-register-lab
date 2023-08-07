#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount  
        self.total = 0
        self.items = []
        self.transactions = []

    def add_item(self, item, price=0, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.transactions.append(
            {"item": item, "quantity": quantity, "price": price}
        )
        
    def apply_discount(self):
        if self.discount:
            self.total = int(self.total * ((100 - self.discount) / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.transactions:
            return "There are no transactions to void."
        self.total -= (
            self.transactions[-1]["price"] * self.transactions[-1]["quantity"]
        )
        for _ in range(self.transactions[-1]["quantity"]):
            self.items.pop()
        self.transactions.pop()
