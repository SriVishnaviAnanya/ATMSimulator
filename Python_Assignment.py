import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM Interface")
        self.root.geometry("400x400")
        self.root.configure(bg="lightgray")  

        self.users = {
            "123456": {"pin": "7890", "balance": 5000, "transactions": []},
            "654321": {"pin": "4321", "balance": 3000, "transactions": []}
        }
        self.current_user = None

        self.create_login_screen()

    def create_login_screen(self):
        """ Creates login screen for the ATM """
        self.clear_screen()
        tk.Label(self.root, text="Enter Card Number", fg="black", bg="lightgray").pack()
        self.card_entry = tk.Entry(self.root, fg="black", bg="white")
        self.card_entry.pack()

        tk.Label(self.root, text="Enter PIN", fg="black", bg="lightgray").pack()
        self.pin_entry = tk.Entry(self.root, show="*", fg="black", bg="white")
        self.pin_entry.pack()

        tk.Button(self.root, text="Login", bg="blue", fg="white", command=self.authenticate).pack()

    def authenticate(self):
        """ Authenticates the user using card number and PIN """
        card_number = self.card_entry.get()
        pin = self.pin_entry.get()

        if card_number in self.users and self.users[card_number]['pin'] == pin:
            self.current_user = card_number
            messagebox.showinfo("Login Successful", "Welcome to the ATM!")
            self.create_main_menu()
        else:
            messagebox.showerror("Error", "Incorrect Card Number or PIN")

    def create_main_menu(self):
        """ Displays the ATM main menu """
        self.clear_screen()
        tk.Button(self.root, text="Check Balance", bg="green", fg="white", command=self.check_balance).pack()
        tk.Button(self.root, text="Deposit Money", bg="blue", fg="white", command=self.deposit_money).pack()
        tk.Button(self.root, text="Withdraw Money", bg="red", fg="white", command=self.withdraw_money).pack()
        tk.Button(self.root, text="Transaction History", bg="purple", fg="white", command=self.transaction_history).pack()
        tk.Button(self.root, text="Logout", bg="black", fg="white", command=self.create_login_screen).pack()

    def check_balance(self):
        """ Displays user's balance """
        balance = self.users[self.current_user]['balance']
        messagebox.showinfo("Balance", f"Your current balance is ₹{balance}")

    def deposit_money(self):
        """ Deposits money into the account """
        self.transaction_window("Deposit Amount", self.deposit)

    def withdraw_money(self):
        """ Withdraws money from the account """
        self.transaction_window("Withdraw Amount", self.withdraw)

    def transaction_window(self, title, transaction_function):
        """ Creates a transaction window for deposits and withdrawals """
        amount_window = tk.Toplevel(self.root)
        amount_window.title(title)
        amount_window.configure(bg="lightyellow")  
        tk.Label(amount_window, text=title, bg="lightyellow").pack()
        amount_entry = tk.Entry(amount_window, fg="black", bg="white")
        amount_entry.pack()

        def submit():
            try:
                amount = int(amount_entry.get())
                transaction_function(amount)
                amount_window.destroy()
            except ValueError:
                messagebox.showerror("Error", "Enter a valid amount")

        tk.Button(amount_window, text="Submit", bg="blue", fg="white", command=submit).pack()

    def deposit(self, amount):
        """ Performs deposit operation """
        if amount > 0:
            self.users[self.current_user]['balance'] += amount
            self.users[self.current_user]['transactions'].append(f"Deposited ₹{amount}")
            messagebox.showinfo("Success", f"₹{amount} deposited successfully!")
        else:
            messagebox.showerror("Error", "Invalid amount!")

    def withdraw(self, amount):
        """ Performs withdrawal operation """
        if 0 < amount <= self.users[self.current_user]['balance']:
            self.users[self.current_user]['balance'] -= amount
            self.users[self.current_user]['transactions'].append(f"Withdrew ₹{amount}")
            messagebox.showinfo("Success", f"₹{amount} withdrawn successfully!")
        else:
            messagebox.showerror("Error", "Insufficient balance or invalid amount!")

    def transaction_history(self):
        """ Displays transaction history """
        history = self.users[self.current_user]['transactions']
        history_text = "\n".join(history) if history else "No transactions yet."
        messagebox.showinfo("Transaction History", history_text)

    def clear_screen(self):
        """ Clears the screen for new UI elements """
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    atm = ATM(root)
    root.mainloop()
