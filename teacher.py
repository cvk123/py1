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

## age sections
label_age = Label(root, text="Age: ", font=("Arial", 20), bg="#121212", fg="white")
label_age.grid(row=2, column=0)

entry_age = Entry(root, font=("Arial", 15))
entry_age.grid(row=2, column=1)

## address sections
label_address = Label(root, text="Address: ", font=("Arial", 20), bg="#121212", fg="white")
label_address.grid(row=3, column=0)

entry_address = Entry(root, font=("Arial", 15))
entry_address.grid(row=3, column=1)

root.mainloop()