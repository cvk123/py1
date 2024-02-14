from tkinter import *
import psycopg2

root = Tk()
root.title("Teacher Registration Form")
root.geometry("900x900")
root.config(bg="#121212")

# Function
def insert_data(name, age, adress):
  conn = psycopg2.connect(
      dbname='student',
      user='postgres',
      password='admin123',
      host='localhost',
      port='5432'
    )
  
  cur = conn.cursor()
  query = ("INSERT INTO teacher (NAME, AGE, ADDRESS) VALUES (%s, %s, %s)")
  cur.execute(query, (name, age, adress))
  conn.commit()
  conn.close()


# LABELS, ENTRIES
label_general = Label(root, text="Add data", font=("Arial", 20), bg="#121212", fg="white")
label_general.grid(row=0, column=1)

# names sections
label_name = Label(root, text="Name: ", font=("Arial", 20), bg="#121212", fg="white")
label_name.grid(row=1, column=0)

entry_name = Entry(root, font=("Arial", 15))
entry_name.grid(row=1, column=1)

# age sections
label_age = Label(root, text="Age: ", font=("Arial", 20), bg="#121212", fg="white")
label_age.grid(row=2, column=0)

entry_age = Entry(root, font=("Arial", 15))
entry_age.grid(row=2, column=1)

# address sections
label_address = Label(root, text="Address: ", font=("Arial", 20), bg="#121212", fg="white")
label_address.grid(row=3, column=0)

entry_address = Entry(root, font=("Arial", 15))
entry_address.grid(row=3, column=1)

# button submit
button = Button(root, text="Submit", font=("Arial", 15), command=lambda:insert_data(entry_name.get(), entry_age.get(), entry_address.get()))
button.grid(row=4, column=1)

# Search data
# general label
label_search = Label(root, text="Search data", font=("Arial", 20), bg="#121212", fg="white")
label_search.grid(row=5, column=1)

# ID section
label_id = Label(root, text="Search by ID: ", font=("Arial", 20), bg="#121212", fg="white")
label_id.grid(row=6, column=0)

entry_id = Entry(root, font=("Arial", 15))
entry_id.grid(row=6, column=1)

# button search
button_search = Button(root, text="Search", font=("Arial", 10))
button_search.grid(row=6, column=2)

root.mainloop()