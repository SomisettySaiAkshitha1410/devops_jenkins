
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class UserSystem:
    def __init__(self):
        self.users = {}
        self.window = tk.Tk()
        self.window.title("Registration and Login Form")

        # Create tabs
        self.tab_control = ttk.Notebook(self.window)
        self.registration_tab = ttk.Frame(self.tab_control)
        self.login_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.registration_tab, text="Registration")
        self.tab_control.add(self.login_tab, text="Login")
        self.tab_control.pack(expand=1, fill="both")

        # Registration form
        self.registration_form()

        # Login form
        self.login_form()

    def registration_form(self):
        # Create registration form widgets
        tk.Label(self.registration_tab, text="Username:").grid(row=0, column=0)
        tk.Label(self.registration_tab, text="Password:").grid(row=1, column=0)
        tk.Label(self.registration_tab, text="Confirm Password:").grid(row=2, column=0)

        self.registration_username = tk.StringVar()
        self.registration_password = tk.StringVar()
        self.registration_confirm_password = tk.StringVar()

        tk.Entry(self.registration_tab, textvariable=self.registration_username).grid(row=0, column=1)
        tk.Entry(self.registration_tab, textvariable=self.registration_password, show="*").grid(row=1, column=1)
        tk.Entry(self.registration_tab, textvariable=self.registration_confirm_password, show="*").grid(row=2, column=1)

        tk.Button(self.registration_tab, text="Register", command=self.register).grid(row=3, column=0, columnspan=2)

    def login_form(self):
        # Create login form widgets
        tk.Label(self.login_tab, text="Username:").grid(row=0, column=0)
        tk.Label(self.login_tab, text="Password:").grid(row=1, column=0)

        self.login_username = tk.StringVar()
        self.login_password = tk.StringVar()

        tk.Entry(self.login_tab, textvariable=self.login_username).grid(row=0, column=1)
        tk.Entry(self.login_tab, textvariable=self.login_password, show="*").grid(row=1, column=1)

        tk.Button(self.login_tab, text="Login", command=self.login).grid(row=2, column=0, columnspan=2)

    def register(self):
        # Register a new user
        username = self.registration_username.get()
        password = self.registration_password.get()
        confirm_password = self.registration_confirm_password.get()

        if username in self.users:
            messagebox.showerror("Error", "Username already exists. Please choose a different username.")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match. Please try again.")
        else:
            self.users[username] = password
            messagebox.showinfo("Success", "Registration successful!")

    def login(self):
        # Login to the system
        username = self.login_username.get()
        password = self.login_password.get()

        if username in self.users and self.users[username] == password:
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid username or password.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    user_system = UserSystem()
    user_system.run()