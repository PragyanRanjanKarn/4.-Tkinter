#Personal Details
import tkinter as tk

T = tk.Tk()
T.title("Personal Details")

frame = tk.LabelFrame(T, text="Personal Details", padx=10, pady=10, bg="lightblue")
frame.pack(padx=10, pady=10)

labels = ["Name", "Age", "Gender", "Email"]
entries = []

for i in range(len(labels)):    
    label = labels[i]
    tk.Label(frame, text=label, bg="lightblue", fg="darkblue").grid(row=i, column=0, sticky="w")
    entry = tk.Entry(frame, bg="white", fg="black")
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries.append(entry)
    
button = tk.Button(frame, text="Submit", bg="darkblue", fg="white")
button.grid(row=len(labels), column=0, pady=10, sticky="w")
T.mainloop()
