# #fruit=["mango", "cashew", "orange", "watermelon", "guava"]
# #print(fruit)
# #computer starts counting from 0
# #last item in a list is -1 and second to  last -2 and so on
# #print(fruit[-2])
# #the lenght of the list is len
# #print(len(fruit))
# #slicing of list
# #print(fruit[0:3])
# #print(fruit[0:-1])
# #0: is to the end of the list and :
# #print(fruit[0:])
# #print(fruit[:3])
# # use .append to add to a list
# #fruit.append("carrot")
# #print(fruit)
# #to remove from list you use .remove
# #fruit.remove("mango")
# #print(fruit)
#
# # LOOPING
# #for x in fruit:
# #   print(x)
# #i=0
# #while(i<len(fruit)):
# #   print(fruit[i])
# #    i=i+1
# #numb=[]
# #i=0
# #while(i<10):
# #    numb.append(i)
# #    i=i+1
# #print(numb)
#
# #even_numb=[]
# #i=2
# # while(i<=20):
# #     even_numb.append(i)
# #     i=i+2
# # print(even_numb)
#
# # odd=[]
# # i=1
# # while(i<=20):
# #     if(i%2>0):
# #         odd.append(i)
# #     i=i+1
# #
# #
# # odd[-1]=21
# # print(odd)
#
# # person={
# #     "name": "Solomon",
# #     "age": 15,
# #     "state": "Edo"
# # }
# # print(person["name"])
# #
# # for i, x in person.items():
# #     print(i, ":", x)
#
# # persons=[
# #     {
# #         "name":"Solomon",
# #         "age": 15,
# #         "state":"edo"
# #     },
# #     {
# #         "name":"Aliyu",
# #         "age": 18,
# #         "state":"Kano"
# #     },
# #     {
# #         "name":"Shafeeq",
# #         "age": 25,
# #         "state":"Oyo"
# #     }
# # ]
#
# # for i in persons:
# #     for x,y in i.items():
# #         print(x, ":", y)
# #list by coding all prime numbers between 1 and 30
#
# # for i in range(2, 20, 3):
# #     print(i)
# # casting is the process of converting one data type to another
# # score1=input("Enter your'e math score")
# # score2=input("Enter youre english score")
# #
# # total=int(score1) + int(score2)
# # print("Youre total score is ", total)
#
# # def display(x):
# #     print("The number you entered is ", x)
# #
# # display(6)
# # element=[2, 3, 4, 5, 6]
# # display(element)
#
# # import math
# # print(math.sqrt(4))
#
# # class House():
# #     def cover(self):
# #         print("I am meant to cover everyone")
# # object1=House()
# # object1.cover()
#
# # class Parent():
# #     def pcolor(self):
# #         print("This is a parent color")
# #
# # class Child(Parent):
# #     def ccolor(self):
# # #         print("This is a child color")
# #
# # p1=Parent()
# # p1.pcolor()
# #
# # c1=Child()
# # c1.pcolor()
# #list prime numbers from 2-30 by coding
# # import time
# # from threading import Thread
# # class Student1(Thread):
# #     def run(self):
# #         for i in range(10):
# #             print("count1 running")
# #             time.sleep(1)
# # s1=Student1()
# # s1.start()
# #
# # class Student2(Thread):
# #     def run(self):
# #         for i in range(10):
# #             print("count2 running")
# #             time.sleep(1)
# # s2=Student2()
# # s2.start()
#
# # class test():
# #     def __init__(self):
# #         print("init method running")
# #     def task(self):
# #         print("task running")
# # t=test()
# # t.task()
#
# from tkinter import *
# from tkinter import messagebox
# from tkinter import filedialog
# from tkinter import colorchooser
# root = Tk()
# root.title("Student Management System")
# root.geometry("400x300")
#
# def display():
#     messagebox.showinfo("Action","You just clicked a button")
#     messagebox.askyesno("Action", "Do you wish to continue youre application")
#     messagebox.askyesnocancel("Action", "Continue")
#     filedialog.askdirectory()
#     colorchooser.askcolor()
# label1=Label(root, text="Welcome to GUI")
# label1.pack()
# b1=Button(root, text="Click Me", command=display)
# b1.pack()
# e1=Entry(root)
# e1.pack()
# root.mainloop()
# file=open("shafeek.txt","w")
#
# file.write("This is my first test")


