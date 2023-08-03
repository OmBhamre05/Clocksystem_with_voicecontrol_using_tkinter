from tkinter import*

def sleepzyas():
    root.destroy()
    import sleepzy 
def voice():
    root.destroy()
    import voicewitgui
def count():
    root.destroy()
    import countdowngui
def Laps():
    root.destroy()
    import lapswithgui
def quiz():
    root.destroy()
    import interactivequiz1
def withalarm():
    root.destroy()
    import quizwithalarm
root= Tk()
root.geometry('700x700')
frame=Frame(root)
frame.pack()
Lab1= Label(frame,text="Welcome to sleepzy",font="Helvetica 20 bold",fg='black').pack(pady=2)
but1= Button(frame,text="Basic Alarm",font="Helvetica 20 bold",fg='green',command=sleepzyas).pack(pady=2)
but4= Button(frame,text="voice control",font="Helvetica 20 bold",fg='green',command=voice).pack(pady=2)
but2= Button(frame,text="Countdown",font="Helvetica 20 bold",fg='green',command=count).pack(pady=2)
but3= Button(frame,text="Laps",font="Helvetica 20 bold",fg='green',command=Laps).pack(pady=2)
but4= Button(frame,text="Quiz",font="Helvetica 20 bold",fg='green',command=quiz).pack(pady=2)
but5= Button(frame,text="Quiz with Alarm",font="Helvetica 20 bold",fg='green',command=withalarm).pack(pady=2)

root.mainloop()