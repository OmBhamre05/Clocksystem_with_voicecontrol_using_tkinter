print("Hello,Welcome to the quiz, Answer the question below to stop the alarm")
from tkinter import *
from tkinter import ttk 
import tkinter as tk
y = 0
i=0
a = ttk.Notebook()

frame1= ttk.Frame(a)
frame2= ttk.Frame(a)
frame3= ttk.Frame(a)
frame4= ttk.Frame(a)
frame5= ttk.Frame(a)
root = ttk.Frame(a)

def quiz(a):
    a.add(frame1, text="Question 1")
    a.add(frame2, text="Question 2")
    a.add(frame3, text="Question 3")
    a.add(frame4, text="Question 4")
    a.add(frame5, text="Question 5")

    Label(frame1, text="What is the value of X in the equation 5X + 3 = 28?",font=("Arial",15,"bold")).grid(row=2,column=2)
    Button(frame1,text="5",font=("Arial",20,"bold"),bg="light blue",command=a_right).grid(row=3,column=1)
    Button(frame1,text="3",font=("Arial",20,"bold"),bg="light pink",command=a_Wrong).grid(row=3,column=2)
    Button(frame1,text="7",font=("Arial",20,"bold"),bg="light yellow",command=a_Wrong).grid(row=3,column=3)
    Button(frame1,text="Next",font=("Arial",20,"bold"),bg="green",command=lambda:a.select(frame2)).grid(row=10,column=5)
    
    Label(frame2, text="If John runs for 5 km in 25 minutes, how long will it take him to run 10 km?",font=("Arial",15,"bold")).grid(row=2,column=2)
    Button(frame2,text="55",font=("Arial",20,"bold"),bg="light blue",command=a2_Wrong).grid(row=3,column=1)
    Button(frame2,text="50",font=("Arial",20,"bold"),bg="light pink",command=a2_right).grid(row=3,column=2)
    Button(frame2,text="45",font=("Arial",20,"bold"),bg="light yellow",command=a2_Wrong).grid(row=3,column=3)
    Button(frame2,text="Next",font=("Arial",20,"bold"),bg="green",command=lambda:a.select(frame3)).grid(row=10,column=5)

    Label(frame3, text="What is the next number in the series: 3, 6, 11, 18, 27, ... ?",font=("Arial",15,"bold")).grid(row=2,column=2)
    Button(frame3,text="38",font=("Arial",20,"bold"),bg="lightpink",command=a3_right).grid(row=3,column=2)
    Button(frame3,text="34",font=("Arial",20,"bold"),bg="light yellow",command=a3_Wrong).grid(row=3,column=3)
    Button(frame3,text="39",font=("Arial",20,"bold"),bg="light pink",command=a3_Wrong).grid(row=3,column=5)
    Button(frame3,text="Next",font=("Arial",20,"bold"),bg="green",command=lambda:a.select(frame4)).grid(row=10,column=5)
    

    Label(frame4,text="12*5+2-(10*2)?",font=("Arial",15,"bold")).grid(row=2,column=2)
    Button(frame4,text="44",font=("Arial",20,"bold"),bg="light blue",command=a4_Wrong).grid(row=3,column=1)
    Button(frame4,text="89",font=("Arial",20,"bold"),bg="light pink",command=a4_Wrong).grid(row=3,column=2)
    Button(frame4,text="42",font=("Arial",20,"bold"),bg="light yellow",command=a4_right).grid(row=3,column=3)
    Button(frame4,text="Next",font=("Arial",20,"bold"),bg="green",command=lambda:a.select(frame5)).grid(row=10,column=5)

    Label(frame5, text="If a worker can do a job in 10 hours, how long will it take two workers to do the same job?",font=("Arial",15,"bold")).grid(row=2,column=2)
    Button(frame5,text="6",font=("Arial",20,"bold"),bg="light blue",command=a5_Wrong).grid(row=3,column=1)
    Button(frame5,text="5",font=("Arial",20,"bold"),bg="light pink",command=a5_right).grid(row=3,column=2)
    Button(frame5,text="15",font=("Arial",20,"bold"),bg="light yellow",command=a5_Wrong).grid(row=3,column=3)
    Button(frame5,text="Next",font=("Arial",20,"bold"),bg="green",command=lambda:a.select(frame5)).grid(row=10,column=5)

marks_obtained = 0

def a_right():
    global marks_obtained
    Label(frame1,text="Correct!",font=("Arial",15,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    marks_obtained += 1
    Label(frame1,text="Marks Obtained : {}".format(marks_obtained),font=("Arial",15,"bold"),background="Red",fg="yellow").grid(row=1,column=3)

def a_Wrong():
    Label(frame1,text="InCorrect!",font=("Arial",15,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame1,text="Marks Obtained : {}".format(marks_obtained),font=("Arial",15,"bold"),background="Red",fg="yellow").grid(row=1,column=3)
    
def a2_right():
    global marks_obtained
    Label(frame2,text="Correct!",font=("Arial",15,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    marks_obtained += 1
    Label(frame2,text="Marks Obtained : {}".format(marks_obtained),font=("Arial",15,"bold"),background="Red",fg="yellow").grid(row=1,column=3)

def a2_Wrong():
    Label(frame2,text="InCorrect!",font=("Arial",15,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame2,text="Marks Obtained : {}".format(marks_obtained),font=("Arial",15,"bold"),background="Red",fg="yellow").grid(row=1,column=3)

def a3_right():
    global marks_obtained
    Label(frame3,text="Correct!",font=("Arial",15,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    marks_obtained += 1
    Label(frame3,text="Marks Obtained : {}".format(marks_obtained),font=("Arial",15,"bold"),background="Red",fg="yellow").grid(row=1,column=3)

def a3_Wrong():
    Label(frame3,text="InCorrect!",font=("Arial",15,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame3,text="Marks Obtained : {}".format(marks_obtained),font=("Arial",15,"bold"),background="Red",fg="yellow").grid(row=1,column=3)

def a4_right():
    global marks_obtained
    Label(frame4,text="Correct!",font=("Arial",15,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    marks_obtained += 1
    Label(frame4,text="Marks Obtained : {}".format(marks_obtained),font=("Arial",15,"bold"),background="Red",fg="yellow").grid(row=1,column=3)
def a4_Wrong():
    Label(frame3,text="InCorrect!",font=("Arial",15,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame3,text="Marks Obtained : {}".format(marks_obtained),font=("Arial",15,"bold"),background="Red",fg="yellow").grid(row=1,column=3)

def a5_right():
    global marks_obtained
    Label(frame5,text="Correct!",font=("Arial",15,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    marks_obtained += 1
    Label(frame5,text="Marks Obtained : {}".format(marks_obtained),font=("Arial",15,"bold"),background="Red",fg="yellow").grid(row=1,column=3)

def a5_Wrong():
    Label(frame5,text="InCorrect!",font=("Arial",15,"bold"),background="green",fg="yellow").grid(row=1,column=2)
    Label(frame5,text="Marks Obtained : {}".format(marks_obtained),font=("Arial",15,"bold"),background="Red",fg="yellow").grid(row=1,column=3)


quiz(a)
a.pack()
quiz(a)
root.mainloop()
