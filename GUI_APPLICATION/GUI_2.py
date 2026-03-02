import tkinter as tk


def calculate():
    num1 = int(entry1.get())
    num2 = int(entry2.get())

    result = num1 + num2
    label.config(text=f"Result = {result}")


root = tk.Tk()
root.geometry("400x250")
root.title("Addition App")
root.config(bg="black")


# ----- Row 0 : Labels -----
tk.Label(
    root,
    text="Number 1",
    bg="black",
    fg="lightgreen",
    font=("Arial", 12)
).grid(row=0, column=0, padx=20, pady=10)

tk.Label(
    root,
    text="Number 2",
    bg="black",
    fg="lightgreen",
    font=("Arial", 12)
).grid(row=0, column=1, padx=20, pady=10)


# ----- Row 1 : Entry Fields -----
entry1 = tk.Entry(root, width=15, font=("Arial", 12), bd=4, relief="solid")
entry1.grid(row=1, column=0, padx=20)

entry2 = tk.Entry(root, width=15, font=("Arial", 12), bd=4, relief="solid")
entry2.grid(row=1, column=1, padx=20)


# ----- Row 2 : Center Button -----
tk.Button(
    root,
    text="Add",
    command=calculate,
    bg="lightblue",
    fg="black",
    font=("Arial", 12, "bold")
).grid(row=2, column=0, columnspan=2, pady=15)


# ----- Row 3 : Output -----
label = tk.Label(
    root,
    text="Output will be here",
    bg="black",
    fg="yellow",
    font=("Arial", 13, "bold")
)
label.grid(row=3, column=0, columnspan=2, pady=10)


root.mainloop()