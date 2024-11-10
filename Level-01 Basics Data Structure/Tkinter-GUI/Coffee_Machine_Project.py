from tkinter import *
from tkinter import messagebox


class CoffeeMachine:
    def __init__(self):
        self.window = Tk()
        self.window.title("Coffee Maker")

        self.MENU = {
            "espresso": {
                "ingredients": {
                    "water": 50,
                    "coffee": 18,
                },
                "cost": 1.5,
            },
            "latte": {
                "ingredients": {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
                "cost": 2.5,
            },
            "cappuccino": {
                "ingredients": {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
                "cost": 3.0,
            }
        }

        self.profit = 0
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

        self.create_widgets()
        self.window.mainloop()

    def create_widgets(self):
        Label(self.window, text="Menu").grid(row=0, column=0)

        for i, (drink, details) in enumerate(self.MENU.items()):
            price = details["cost"]
            Label(self.window, text=f"{drink}: ${price}").grid(row=i + 1, column=0)

        Label(self.window, text="Order").grid(row=0, column=1)
        self.order_var = StringVar(value=list(self.MENU.keys())[0])
        OptionMenu(self.window, self.order_var, *self.MENU.keys()).grid(row=1, column=1)

        Label(self.window, text="Coins").grid(row=2, column=1)
        self.coin_entry = Entry(self.window)
        self.coin_entry.grid(row=3, column=1)

        Button(self.window, text="Order", command=self.order).grid(row=4, column=1)
        Button(self.window, text="Report", command=self.report).grid(row=5, column=1)

    def order(self):
        drink = self.order_var.get()
        try:
            coins = float(self.coin_entry.get())
            price = self.MENU[drink]["cost"]

            if coins < price:
                messagebox.showerror("Error", "Insufficient coins")
                return

            ingredients = self.MENU[drink]["ingredients"]

            if self.check_resources(ingredients):
                self.reduce_resources(ingredients)  # Deduct resources
                change = round(coins - price, 2)
                self.profit += price
                messagebox.showinfo("Success", f"Here is your {drink}. Change: ${change}")
            else:
                messagebox.showerror("Error", "Not enough resources")
        except:
            messagebox.showerror("Error", "Enter a value into the box")

    def check_resources(self, ingredients):
        for item, amount in ingredients.items():
            if self.resources[item] < amount:
                return False
        return True

    def reduce_resources(self, ingredients):
        for item, amount in ingredients.items():
            self.resources[item] -= amount  # Deduct the required amount

    def report(self):
        messagebox.showinfo(
            "Report",
            f"Water: {self.resources['water']}ml\n"
            f"Milk: {self.resources['milk']}ml\n"
            f"Coffee: {self.resources['coffee']}g\n"
            f"Profit: ${self.profit}"
        )


if __name__ == "__main__":
    CoffeeMachine()
