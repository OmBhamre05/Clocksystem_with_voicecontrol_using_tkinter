import time
import tkinter as tk

def start_timer():
    starttime = time.time()
    lasttime = starttime
    lapnum = 1
    
    def record_lap():
        nonlocal lasttime, lapnum
        laptime = round((time.time() - lasttime), 2)
        totaltime = round((time.time() - starttime), 2)
        lap_text.set("Lap No. " + str(lapnum) + "\nTotal Time: " + str(totaltime) + "\nLap Time: " + str(laptime))
        lasttime = time.time()
        lapnum += 1

    lap_text = tk.StringVar()
    lap_text.set("Press the Lap button to count laps.")
    
    lap_label = tk.Label(root, textvariable=lap_text)
    lap_label.pack()
    
    lap_button = tk.Button(root, text="Lap",font="Helvetica 20 bold", command=record_lap)
    lap_button.pack()

root = tk.Tk()
root.title("Timer")
root.geometry('1000x600')

start_timer()

root.mainloop()
