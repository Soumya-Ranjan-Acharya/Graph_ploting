import tkinter as tk
#creating main window
root=tk.Tk()
root.title("V.O.I.C.E your assistant")
root.geometry("400x400")
label=tk.Label(root,text="soumya's assistant")
label.pack()
def say_hello():
    print("hello Sir, how can I help you?")
btn=tk.Button(root,text="click me",command=say_hello)
btn.pack(pady=10)
root.mainloop()



