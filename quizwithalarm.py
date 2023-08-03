
#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import datetime
import time
from threading import*

def run1():
        y= 0
        for y in range(0,2):
           from interactivequiz1 import marks_obtained
           if(marks_obtained<3):  
               from playsound import playsound   
               playsound("sound1.wav")  
               import interactivequiz1 as sd
               print('playing sound using playsound')
               y=y+1
           else:
                from playsound import playsound   
                playsound("sound2.wav")  
                exit()
def run2():
    y=0
    for y in range(0,2):
        if(y<3):
            from playsound import playsound
            playsound("sound1.wav")
        else:
            from playsound import playsound
            playsound("sound2.wav")
t1=Thread(target=run1)
t2=Thread(target=run2)


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake up")
            clock.destroy()
            t1.start()
            t2.start()

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("DataFlair Alarm Clock")
clock.geometry("900x1200")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial 20 bold").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)

clock.mainloop()
#Execution of the window.

