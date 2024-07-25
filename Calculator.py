from tkinter import *




root=Tk()
root.geometry("350x400")
root.title("Electronic Calculator")
root.resizable(False, False)
e1=Entry(root, width=100, font=("Arial 18"))
e1.place(x=2, y=2)

def show1(x):
    e1.insert(END, x)

def wipe():
    e1.delete(0, END)

def result():
    answer=eval(e1.get())
    e1.delete(0, END)
    e1.insert(END, answer)

b9=Button(root, width=8, height=5, text="9", bg="white", command=lambda:show1(9))
b8=Button(root, width=8, height=5, text="8", bg="white", command=lambda:show1(8))
b7=Button(root, width=8, height=5, text="7", bg="white", command=lambda:show1(7))
b6=Button(root, width=8, height=5, text="6", bg="white", command=lambda:show1(6))
b5=Button(root, width=8, height=5, text="5", bg="white", command=lambda:show1(5))
b4=Button(root, width=8, height=5, text="4", bg="white", command=lambda:show1(4))
b3=Button(root, width=8, height=5, text="3", bg="white", command=lambda:show1(3))
b2=Button(root, width=8, height=5, text="2", bg="white", command=lambda:show1(2))
b1=Button(root, width=8, height=5, text="1", bg="white", command=lambda:show1(1))
b0=Button(root, width=8, height=5, text="0", bg="white", command=lambda:show1(0))
bplus=Button(root, width=15, height=2, text="+", bg="white", command=lambda:show1("+"))
bminus=Button(root, width=15, height=2, text="-", bg="white", command=lambda:show1("-"))
btimes=Button(root, width=15, height=2, text="x", bg="white", command=lambda:show1("*"))
bdivide=Button(root, width=15, height=2, text="/", bg="white", command=lambda:show1("/"))
bequals=Button(root, width=15, height=5, text="=", bg="white", command=lambda:result())
bclear=Button(root, width=43, height=2, text="clear", bg="white", command=wipe)

b7.place(x=5, y=40)
b8.place(x=70, y=40)
b9.place(x=135, y=40)

b4.place(x=5, y=140)
b5.place(x=70, y=140)
b6.place(x=135, y=140)

b1.place(x=5, y=240)
b2.place(x=70, y=240)
b3.place(x=135, y=240)

bplus.place(x=203, y=40)
bminus.place(x=203, y=84)
btimes.place(x=203, y=140)

bdivide.place(x=203, y=184)
bequals.place(x=203, y=240)
bclear.place(x=5, y=329)
root.mainloop()
