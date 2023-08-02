from tkinter import Tk

def login(username, password):
    usn = username.get()
    pwd = password.get()

    if usn == '' or pwd == '':
        message.set("Fill the empty field!")
    else:
        if usn == "llcj_69" and pwd == "1amPan0T":
            message.set("Login success!")
        else:
            message.set("Invalid Login [Incorrect username or password]")

def create_login_form():
    login_screen = Tk()
    login_screen.title("Login Form")
    login_screen.geometry("300x250")

    message = StringVar()
    username = StringVar()
    password = StringVar()

    Label(login_screen, width="300", text="Please enter details below", bg="orange", fg="white").pack()

    Label(login_screen, text="Username:").place(x=20, y=40)
    Entry(login_screen, textvariable=username).place(x=90, y=42)

    Label(login_screen, text="Password: ").place(x=20, y=80)
    Entry(login_screen, textvariable=password, show="*").place(x=90, y=79)

    Label(login_screen, text="", textvariable=message).place(x=30, y=100)
    Button(login_screen, text="Login",)

