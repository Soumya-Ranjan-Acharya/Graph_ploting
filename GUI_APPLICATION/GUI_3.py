import tkinter as tk


root = tk.Tk()
root.geometry("400x300")
root.title("Addition App")
'''relief="flat"
relief="solid"
relief="raised"
relief="sunken"
relief="ridge"
relief="groove"
'''
entry = tk.Entry(root, relief="raised", bd=4)
entry.pack(pady=20)
entry.place(x=10,y=30)
root.config(bg="black")
root.mainloop()