from tkinter import *
import psycopg2

root = Tk()
root.title("Teacher Registration Form")
root.geometry("900x900")
root.config(bg="#121212")

## LABELS, ENTRIES
label_general = Label(root, text="Add data", font=("Arial", 20), bg="#121212", fg="white")
label_general.grid(row=0, column=1)

## names sections
label_name = Label(root, text="Name: ", font=("Arial", 20), bg="#121212", fg="white")
label_name.grid(row=1, column=0)

entry_name = Entry(root, font=("Arial", 15))
entry_name.grid(row=1, column=1)

root.mainloop()