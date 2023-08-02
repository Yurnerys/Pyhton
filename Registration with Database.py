import tkinter as tk
import mysql.connector




def register():

    conn = mysql.connector.connect(host="sql6.freesqldatabase.com",port="3306", user="sql6633328",password="Hph56TuQYd",database="")
    
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    
    conn = sqlite3.connect('registration.db')
    c = conn.cursor()

    
    c.execute('''CREATE TABLE USERS (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    password TEXT
                )''')

    
    c.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
              (name, email, password))
    conn.commit()
    conn.close()

    
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    print("User registered successfully!")


window = tk.Tk()
window.title("Registration Form")


name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

email_label = tk.Label(window, text="Email:")
email_label.pack()
email_entry = tk.Entry(window)
email_entry.pack()

password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

register_button = tk.Button(window, text="Register", command=register)
register_button.pack()


window.mainloop()
