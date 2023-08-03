import time
from tkinter import *
from tkinter import messagebox
import winsound
root = Tk()
root.geometry("600x600")
root.title("Time Counter")
root.configure(background="white")
hour=StringVar()
minute=StringVar()
second=StringVar()

hour.set("01")
minute.set("00")
second.set("00")
sac2=Button(root,text='hr',width=2,height=1,font='calbiri').place(x=85,y=50)
sac3=Button(root,text='min',width=3,height=1,font='calbiri').place(x=130,y=50)
sac4=Button(root,text='sec',width=3,height=1,font='calbiri').place(x=180,y=50)
hourEntry= Entry(root, width=3, font=("calbiri",18,""),
				textvariable=hour)
hourEntry.place(x=80,y=20)

minuteEntry= Entry(root, width=3, font=("calbiri",18,""),
				textvariable=minute)
minuteEntry.place(x=130,y=20)

secondEntry= Entry(root, width=3, font=("calbiri",18,""),
				textvariable=second)
secondEntry.place(x=180,y=20)


def submit():
	try:
		
		time1 = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
	except:
		print("Please input the right value")
	while time1 >-1:
		mins,secs = divmod(time1,60)
		hours=0
		if mins >60:
			hours, mins = divmod(mins, 60)
		hour.set("{0:2d}".format(hours))
		minute.set("{0:2d}".format(mins))
		second.set("{0:2d}".format(secs))
		root.update()
		time.sleep(1)
		if (time1 == 0):
			winsound.Beep(frequency=1300,duration=4000)
			messagebox.showinfo("Time Countdown", "Time's up ")

		time1-= 1

btn = Button(root, text='Set Time Countdown', bd='5',font="Helvetica 10 bold",
			command= submit,bg="dark blue",fg="white")
btn.place(x = 70,y = 120)

root.mainloop()