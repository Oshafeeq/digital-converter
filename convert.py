import math
from tkinter import *

import requests


class Convert():
    def __init__(self):

        root = Tk()
        root.title("Digital Converter")
        root.geometry("1200x600")
        root.resizable(False, False)
        logo=PhotoImage(file="logo.png")
        root.iconphoto(True, logo)


        f1=Frame(root, width=300, height=500, bg="white", highlightbackground="black", highlightthickness="5" )
        f1.place(x=20, y=20)
        image1=PhotoImage(file="Background.png")
        label1= Label(f1, image=image1)
        label1.place(x=0, y=0)
        label2=Label(f1, text="Digital Converter Calculator", font="Arial 14")
        label2.place(x=0, y=300)
        f2=Frame(root, width=330, height=500, bg="white", highlightbackground="black", highlightthickness="5")
        f2.place(x=340, y=20)





        l3=Label(root, text="Electronic Calculator", font="Arial 14")
        l3.place(x=340, y=0)
        e1=Entry(f2, width=100, font=("Arial 18"))
        e1.place(x=2, y=2)

        def show1(x):
            e1.insert(END, x)

        def wipe():
            e1.delete(0, END)

        def result():
            answer=eval(e1.get())
            e1.delete(0, END)
            e1.insert(END, answer)

        b9=Button(f2, width=8, height=5, text="9", bg="white", command=lambda:show1(9))
        b8=Button(f2, width=8, height=5, text="8", bg="white", command=lambda:show1(8))
        b7=Button(f2, width=8, height=5, text="7", bg="white", command=lambda:show1(7))
        b6=Button(f2, width=8, height=5, text="6", bg="white", command=lambda:show1(6))
        b5=Button(f2, width=8, height=5, text="5", bg="white", command=lambda:show1(5))
        b4=Button(f2, width=8, height=5, text="4", bg="white", command=lambda:show1(4))
        b3=Button(f2, width=8, height=5, text="3", bg="white", command=lambda:show1(3))
        b2=Button(f2, width=8, height=5, text="2", bg="white", command=lambda:show1(2))
        b1=Button(f2, width=8, height=5, text="1", bg="white", command=lambda:show1(1))
        b0=Button(f2, width=8, height=5, text="0", bg="white", command=lambda:show1(0))
        bplus=Button(f2, width=15, height=2, text="+", bg="white", command=lambda:show1("+"))
        bminus=Button(f2, width=15, height=2, text="-", bg="white", command=lambda:show1("-"))
        btimes=Button(f2, width=15, height=2, text="x", bg="white", command=lambda:show1("*"))
        bdivide=Button(f2, width=15, height=2, text="/", bg="white", command=lambda:show1("/"))
        bequals=Button(f2, width=15, height=5, text="=", bg="white", command=lambda:result())
        bclear=Button(f2, width=43, height=2, text="clear", bg="white", command=wipe)

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
        f3=Frame(root, width=500, height=500, bg="white", highlightbackground="black", highlightthickness="5")
        f3.place(x=690, y=20)

        def hour ():
            answer = (entry1.get())
            answer = int(answer)
            m = answer*60
            entryt1.delete(0, END)
            entryt1.insert(END, m)


        def decimal ():
            from fractions import Fraction
            answer = (entry2.get())
            answer = float(answer)
            x = Fraction(answer).limit_denominator()
            entryt2.delete(0, END)
            entryt2.insert(END, x)


        def degree ():
            answer = (entry3.get())
            answer = int(answer)
            d = math.radians(answer)
            entryt3.delete(0, END)
            entryt3.insert(END, d)

        def kilometer ():
            answer = (entry4.get())
            answer = int(answer)
            k = answer*1000
            entryt4.delete(0, END)
            entryt4.insert(END, k)

        def celsius ():
            answer = (entry6.get())
            answer = int(answer)
            c = (answer*(9/5)) + 32
            entryt6.delete(0, END)
            entryt6.insert(END, c)

        def dollar1 ():
            import requests
            url = "https://v6.exchangerate-api.com/v6/34813435b764d15f628b80ea/pair/USD/NGN"
            response = requests.get(url)
            data = response.json()
            k = int(entry5.get())
            y = k*data["conversion_rate"]
            entryt5.delete(0, END)
            entryt5.insert(END, y)






        l4=Label(root, text="Digital Converter")
        l4.place()

        entry1=Entry(f3, width=10, font="Arial 18", borderwidth=5)
        entry2=Entry(f3, width=10, font="Arial 18", borderwidth=5)
        entry3=Entry(f3, width=10, font="Arial 18", borderwidth=5)
        entry4=Entry(f3, width=10, font="Arial 18", borderwidth=5)
        entry5=Entry(f3, width=10, font="Arial 18", borderwidth=5)
        entry6=Entry(f3, width=10, font="Arial 18", borderwidth=5)

        entryt1=Entry(f3, width=10, font="Arial 18", borderwidth=5)
        entryt2=Entry(f3, width=10, font="Arial 18", borderwidth=5)
        entryt3=Entry(f3, width=10, font="Arial 18", borderwidth=5)
        entryt4=Entry(f3, width=10, font="Arial 18", borderwidth=5)
        entryt5=Entry(f3, width=10, font="Arial 18", borderwidth=5)
        entryt6=Entry(f3, width=10, font="Arial 18", borderwidth=5)

        bc1=Button(f3, width=10, height=1, text="Convert", bg="yellow", command=hour)
        bc2=Button(f3, width=10, height=1, text="Convert", bg="yellow", command=decimal)
        bc3=Button(f3, width=10, height=1, text="Convert", bg="yellow", command=degree)
        bc4=Button(f3, width=10, height=1, text="Convert", bg="yellow", command=kilometer)
        bc5=Button(f3, width=10, height=1, text="Convert", bg="yellow", command=dollar1)
        bc6=Button(f3, width=10, height=1, text="Convert", bg="yellow", command=celsius)

        entry1.place(x=20, y=70)
        entry2.place(x=20, y=140)
        entry3.place(x=20, y=210)
        entry4.place(x=20, y=280)
        entry5.place(x=20, y=350)
        entry6.place(x=20, y=430)

        bc1.place(x=220, y=70)
        bc2.place(x=220, y=140)
        bc3.place(x=220, y=210)
        bc4.place(x=220, y=280)
        bc5.place(x=220, y=350)
        bc6.place(x=220, y=430)

        entryt1.place(x=340, y=70)
        entryt2.place(x=340, y=140)
        entryt3.place(x=340, y=210)
        entryt4.place(x=340, y=280)
        entryt5.place(x=340, y=350)
        entryt6.place(x=340, y=430)

        lab1=Label(f3, text="Hour to minute")
        lab2=Label(f3, text="Decimal to fractions")
        lab3=Label(f3, text="Degree to radian")
        lab4=Label(f3, text="kilometer to meter")
        lab5=Label(f3, text="Dollar to Naira")
        lab6=Label(f3, text="Celsius to Farenheit")

        lab1.place(x=10, y=47)
        lab2.place(x=10, y=117)
        lab3.place(x=10, y=187)
        lab4.place(x=10, y=257)
        lab5.place(x=10, y=327)
        lab6.place(x=10, y=407)
        name=Label(root, text="Built By Shafeeq", font="Arial 29")
        name.place(x=450, y=540)

        root.mainloop()
o1=Convert()
