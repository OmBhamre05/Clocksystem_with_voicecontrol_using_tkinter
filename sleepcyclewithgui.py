import tkinter as tk

def calculate_wakeup_time():
    hour1 = int(hour_entry.get())
    min1 = int(minute_entry.get())
    z = hour1
    y = min1
    values = range(7)
    for i in values:
        z = z + 1
        y = y + 30
        for i in values:
            if z >= 12:
                z = z - 12
            if y >= 60:
                y = y - 60
        i += 1
        result_label.config(text="You can wake up at {}:{}".format(z, y))

root = tk.Tk()
root.title("Wake Up Time Calculator")

hour_label = tk.Label(root, text="Enter hour:")
hour_label.grid(row=0, column=0, padx=10, pady=10)

hour_entry = tk.Entry(root)
hour_entry.grid(row=0, column=1, padx=10, pady=10)

minute_label = tk.Label(root, text="Enter minute:")
minute_label.grid(row=1, column=0, padx=10, pady=10)

minute_entry = tk.Entry(root)
minute_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate_wakeup_time)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
