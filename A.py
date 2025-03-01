#Personal Details
import tkinter as tk

T = tk.Tk()
T.title("Personal Details")

frame = tk.LabelFrame(T, text="Personal Details", padx=10, pady=10)
frame.pack(padx=10, pady=10)

labels = ["Name", "Age", "Gender", "Email"]
entries = []

for i in range(len(labels)):
    label = labels[i]
    tk.Label(frame, text=label).grid(row=i, column=0, sticky="w")
    entry = tk.Entry(frame)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)

T.mainloop()
