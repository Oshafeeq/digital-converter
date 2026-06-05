from tkinter import *
from tkinter import messagebox


root=Tk()
root.title("Login Page")
root.geometry("370x300")
root.resizable(False, False)
import hashlib

STORED_HASH = hashlib.sha256("Shafeeq".encode()).hexdigest()

def emptyfield():
    user = entry1.get()
    pass1 = entry2.get()
    pass_hash = hashlib.sha256(pass1.encode()).hexdigest()
    if user == "" or pass1 == "":
        messagebox.showinfo("Error message", "Field(s) cannot be left empty")
    elif user != "Shafeeq" or pass_hash != STORED_HASH:
        messagebox.showinfo("wrong info", "Incorrect username and or password")
    else:
        messagebox.showinfo("Login Successful", "transporting to account")
        root.destroy()
        import convert
        convert.Convert()



login=Label(root, text="Login Page", font="Arial 20")
logindetails= Label(root, text="Please enter your login details below")
username=Label(root, text="Username")
password=Label(root, text="Password")
entry1 = Entry(root, width=14, font="Arial 14", borderwidth=2)
entry2 = Entry(root, width=14, font="Arial 14", borderwidth=2)

submit=Button(root, text="Login", bg="green", width=10, fg="white", command=emptyfield)

submit.place(x=110, y=170)
entry1.place(x=110, y=80)
entry2.place(x=110, y=120)
login.place(x=110, y=20)
logindetails.place(x=110, y=53)
username.place(x=40, y=80)
password.place(x=40, y=120)
root.mainloop()

# Application programming interface (API)
# 4 methods of interacting with API
#they are also called http methods
#1. get: used to get info from API server
#2. post: used to send info to the server
#3. put/patch:it is used to update or edit info on the server
#4. delete: is used to remove info from the server
