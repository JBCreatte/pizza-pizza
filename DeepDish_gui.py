import tkinter as tk


class MyApp:
    def __init__(self, root):
        self.canvas = Canvas(root)

        self.image = PhotoImage("gif-of-schmidt-eating-pizza-gif")
        self.canvas.create_image(0, 4, image=image)

        self.image = PhotoImage("thin-eating")
        self.canvas.create_image(4, 4, image=image)



class PizzaCalculator:
    # Calculate base price of the pizza based on the selected size
    def __init__(self, master):
        self.master = master
        self.master.title("Delicious deep dish")

        self.size_label = tk.Label(self.master, text="Pizza Size:")
        self.size_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.size_var = tk.StringVar(self.master)
        self.size_var.set("Small")

        self.size_option = tk.OptionMenu(self.master, self.size_var, "Small", "Medium", "Large")
        self.size_option.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        # Add additional cost for selected toppings
        self.toppings_label = tk.Label(self.master, text="Toppings:")
        self.toppings_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        self.pepperoni_var = tk.IntVar(self.master)
        self.pepperoni_var.set(0)

        self.pepperoni_check = tk.Checkbutton(self.master, text="Pepperoni", variable=self.pepperoni_var)
        self.pepperoni_check.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.sausage_var = tk.IntVar(self.master)
        self.sausage_var.set(0)

        self.sausage_check = tk.Checkbutton(self.master, text="Sausage", variable=self.sausage_var)
        self.sausage_check.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        self.bacon_var = tk.IntVar(self.master)
        self.bacon_var.set(0)

        self.bacon_check = tk.Checkbutton(self.master, text="Bacon", variable=self.bacon_var)
        self.bacon_check.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        self.chicken_var = tk.IntVar(self.master)
        self.chicken_var.set(0)

        self.chicken_check = tk.Checkbutton(self.master, text="Chicken", variable=self.chicken_var)
        self.chicken_check.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

        self.pineapple_var = tk.IntVar(self.master)
        self.pineapple_var.set(0)

        self.pineapple_check = tk.Checkbutton(self.master, text="Pineapple", variable=self.pineapple_var)
        self.pineapple_check.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

        self.mushrooms_var = tk.IntVar(self.master)
        self.mushrooms_var.set(0)

        self.mushrooms_check = tk.Checkbutton(self.master, text="Mushrooms", variable=self.mushrooms_var)
        self.mushrooms_check.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

        self.onions_var = tk.IntVar(self.master)
        self.onions_var.set(0)

        self.onions_check = tk.Checkbutton(self.master, text="Onions", variable=self.onions_var)
        self.onions_check.grid(row=7, column=1, padx=5, pady=5, sticky=tk.W)

        self.xcheese_var = tk.IntVar(self.master)
        self.xcheese_var.set(0)

        self.xcheese_check = tk.Checkbutton(self.master, text="Xcheese", variable=self.xcheese_var)
        self.xcheese_check.grid(row=8, column=1, padx=5, pady=5, sticky=tk.W)

        self.veggies_var = tk.IntVar(self.master)
        self.veggies_var.set(0)

        self.veggies_check = tk.Checkbutton(self.master, text="Veggies", variable=self.veggies_var)
        self.veggies_check.grid(row=9, column=1, padx=5, pady=5, sticky=tk.W)

        self.calculate_button = tk.Button(self.master, text="Calculate Total", command=self.calculate_total)
        self.calculate_button.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

        self.total_label = tk.Label(self.master, text="Total:")
        self.total_label.grid(row=11, column=0, padx=5, pady=5, sticky=tk.W)

        self.total_var = tk.StringVar(self.master)
        self.total_var.set("$0.00")

        self.total_display = tk.Label(self.master, textvariable=self.total_var)
        self.total_display.grid(row=12, column=1, padx=5, pady=5, sticky=tk.W)

        #incorporate an exit button
        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.quit)
        self.exit_button.grid(row=12, column=2, columnspan=2, padx=5, pady=5)

    # Calculate total cost and update display
    def calculate_total(self):
        size = self.size_var.get()
        toppings = []

        if self.pepperoni_var.get():
            toppings.append("Pepperoni")
        if self.sausage_var.get():
            toppings.append("Sausage")
        if self.bacon_var.get():
            toppings.append("Bacon")
        if self.chicken_var.get():
            toppings.append("Chicken")
        if self.pineapple_var.get():
            toppings.append("Pineapple")
        if self.mushrooms_var.get():
            toppings.append("Mushrooms")
        if self.onions_var.get():
            toppings.append("Onions")
        if self.onions_var.get():
            toppings.append("XCheese")
        if self.veggies_var.get():
            toppings.append("Veggies")

        prices = {
            "Small": 10.99,
            "Medium": 14.99,
            "Large": 18.99
        }

        base_price = prices[size]
        topping_price = len(toppings) * 1.99
        total_price = base_price + topping_price

        self.total_var.set(f"${total_price:.2f}")

root = tk.Tk()

app = PizzaCalculator(root)
root.mainloop()
