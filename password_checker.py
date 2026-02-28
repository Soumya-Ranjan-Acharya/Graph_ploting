import re
import tkinter as tk
from tkinter import ttk

# ---- Password logic (same rules) ----
def password_Checker(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if len(re.findall(r"[A-Z]", password)) >= 2:
        score += 1
    if len(re.findall(r"[a-z]", password)) >= 2:
        score += 1
    if len(re.findall(r"[0-9]", password)) >= 2:
        score += 1
    if len(re.findall(r"[!@#$%^&*(),.?\":{}|<>]", password)) >= 2:
        score += 1

    return score


# ---- GUI logic ----
def check_password(event=None):
    pwd = entry.get()
    score = password_Checker(pwd)

    progress['value'] = score * 20

    if score <= 2:
        result_label.config(text="Weak Password", fg="red")
    elif score <= 4:
        result_label.config(text="Medium Password", fg="orange")
    else:
        result_label.config(text="Strong Password", fg="green")


def toggle_password():
    entry.config(show="" if show_var.get() else "*")


def clear_field():
    entry.delete(0, tk.END)
    progress['value'] = 0
    result_label.config(text="")


# ---- Window ----
root = tk.Tk()
root.title("Password Checker")
root.geometry("420x280")
root.config(bg="#1e1e1e")  # dark background

# ---- Frame (layout container) ----
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=20)

tk.Label(frame,
         text="Enter Password",
         font=("Arial", 14, "bold"),
         fg="white",
         bg="#1e1e1e").pack(pady=5)

entry = tk.Entry(frame, show="*", width=30, font=("Arial", 12))
entry.pack()
entry.bind("<KeyRelease>", check_password)

show_var = tk.BooleanVar()
tk.Checkbutton(frame,
               text="Show Password",
               variable=show_var,
               command=toggle_password,
               bg="#1e1e1e",
               fg="white",
               selectcolor="#1e1e1e").pack(pady=5)

progress = ttk.Progressbar(frame,
                            length=300,
                            mode="determinate",
                            maximum=100)
progress.pack(pady=5)

result_label = tk.Label(frame,
                        text="",
                        font=("Arial", 12, "bold"),
                        bg="#1e1e1e")
result_label.pack(pady=5)

tk.Button(frame,
          text="Clear",
          command=clear_field,
          bg="#444",
          fg="white",
          width=10).pack(pady=5)

root.mainloop()