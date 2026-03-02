from tkinter import *
import time

# Create main window
root = Tk()
root.title("Digital Clock")
root.geometry("400x150")
root.resizable(False, False)
root.config(bg="black")

# Label for clock display
label = Label(root, font=("DS-Digital", 50, "bold"), bg="black", fg="cyan")
label.pack(anchor="center", pady=20)
# Label for date display
date_label = Label(root, font=("Arial", 14), bg="black", fg="white")
date_label.pack(anchor="center")

# Function to update time every second
def update_time():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %d %B %Y")
    label.config(text=current_time)
    date_label.config(text=current_date)
    label.after(1000, update_time)  # update every 1 second

    

# Start updating
update_time()

# Run the main loop
root.mainloop()
