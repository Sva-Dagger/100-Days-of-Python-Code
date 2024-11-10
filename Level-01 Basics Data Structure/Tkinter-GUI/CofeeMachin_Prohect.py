from tkinter import Tk, Label, StringVar, OptionMenu, Entry, Button, messagebox

window = Tk()

class CoffeeMachine:
    def __init__(self):
        window.title("Coffee Maker")
        
        self.menu = {
            "Espresso": 1.5,
            "Latte": 2.5,
            "Cappuccino": 3.0
        }
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.profit = 0
        self.create_widget()
        
    def create_widget(self):
        Menu_label = Label(window, text="Menu")
        Menu_label.grid(row=0, column=0)
        
        for i, (drink, price) in enumerate(self.menu.items()):
            Price_label = Label(window, text=f"{drink}: ${price}")
            Price_label.grid(row=i + 1, column=0)
        
        # Order
        Order_label = Label(window, text="Order")
        Order_label.grid(row=0, column=1)
        
        self.order_var = StringVar()
        self.order_var.set(list(self.menu.keys())[0])
        order_menu = OptionMenu(window, self.order_var, *self.menu.keys())  # Add window as the parent
        order_menu.grid(row=1, column=1)
        
        # Coins
        Coins= Label(text="Coins")
        Coins.grid(row=2, column=1)
        self.coin_entry = Entry(window)
        self.coin_entry.grid(row=3, column=1)
        
        # Buttons
        Order_button = Button(text="Order", command=self.order)
        Order_button.grid(row=4, column=1)
        Report_button = Button(text="Report", command=self.report)
        Report_button.grid(row=5, column=1)

    def order(self):
                drink = self.order_var.get()
                price = self.menu[drink]
                coins = float(self.coin_entry.get())
                if coins >= price:
                    change = round(coins - price, 2)
                    messagebox.showinfo("Success", f"Here is your {drink}. Change: ${change}")
                    self.profit += price
                else:
                    messagebox.showerror("Error", "Insufficient coins")
                    self.w
                    
    def report(self):
            messagebox.showinfo("Report", f"Water: {self.resources['water']}ml\nMilk: {self.resources['milk']}ml\nCoffee: {self.resources['coffee']}g\nProfit: ${self.profit}")

if __name__ == "__main__":
    machine = CoffeeMachine()
    
    
window.mainloop()
