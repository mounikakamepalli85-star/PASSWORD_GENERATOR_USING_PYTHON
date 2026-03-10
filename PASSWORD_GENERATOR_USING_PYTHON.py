import tkinter as tk
from tkinter import messagebox
import random
import string


def update_length_label(value):
    length_label.config(text=value)

def generate_password():
    length = int(length_slider.get())
    characters = ""

    if upper_var.get():
        characters += string.ascii_uppercase
    if lower_var.get():
        characters += string.ascii_lowercase
    if number_var.get():
        characters += string.digits
    if symbol_var.get():
        characters += string.punctuation

    if characters == "":
        messagebox.showerror("Error", "Select at least one option")
        return

    password = "".join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    upper_var.set(0)
    lower_var.set(0)
    number_var.set(0)
    symbol_var.set(0)
    length_slider.set(12)
    length_label.config(text="12")

def clear_password():
    password_entry.delete(0, tk.END)

# =========================
# WINDOW
# =========================

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x600")
root.configure(bg="#d79a64")
root.resizable(False, False)


title = tk.Label(root,
                 text="Password Generator",
                 font=("Arial", 22, "bold"),
                 bg="#d79a64")
title.pack(pady=20)



password_entry = tk.Entry(root,
                          font=("Arial", 14),
                          width=28,
                          justify="center")
password_entry.pack(pady=15)



tk.Label(root,
         text="Range Of Characters",
         font=("Arial", 12, "bold"),
         bg="#d79a64").pack()

length_label = tk.Label(root,
                        text="12",
                        font=("Arial", 11),
                        bg="#d79a64")
length_label.pack()

length_slider = tk.Scale(root,
                         from_=6,
                         to=32,
                         orient="horizontal",
                         command=update_length_label,
                         bg="#d79a64",
                         highlightthickness=0)
length_slider.set(12)
length_slider.pack(pady=5)


upper_var = tk.IntVar(value=0)
lower_var = tk.IntVar(value=0)
number_var = tk.IntVar(value=0)
symbol_var = tk.IntVar(value=0)

tk.Checkbutton(root, text="Uppercase",
               variable=upper_var,
               bg="#d79a64").pack(anchor="w", padx=100)

tk.Checkbutton(root, text="Lowercase",
               variable=lower_var,
               bg="#d79a64").pack(anchor="w", padx=100)

tk.Checkbutton(root, text="Numbers",
               variable=number_var,
               bg="#d79a64").pack(anchor="w", padx=100)

tk.Checkbutton(root, text="Symbols",
               variable=symbol_var,
               bg="#d79a64").pack(anchor="w", padx=100)



generate_btn = tk.Button(root,
                         text="Generate Password",
                         font=("Arial", 12, "bold"),
                         bg="#e3e9e8",
                         command=generate_password)
generate_btn.pack(pady=20)

clear_btn = tk.Button(root,
                      text="Clear",
                      font=("Arial", 11, "bold"),
                      bg="#f5d0c5",
                      command=clear_password)
clear_btn.pack()

footer_frame = tk.Frame(root, bg="#d79a64")
footer_frame.pack(side="bottom", pady=20)

tk.Label(footer_frame,
         text="Developed by ",
         bg="#d79a64",
         font=("Arial", 10)).pack(side="left")

tk.Label(footer_frame,
         text="Mounika ",
         fg="#ff0066",
         bg="#d79a64",
         font=("Arial", 10, "bold")).pack(side="left")

tk.Label(footer_frame,
         text="K",
         fg="#0077ff",
         bg="#d79a64",
         font=("Arial", 10, "bold")).pack(side="left")

root.mainloop()

