import tkinter as tk
from tkinter import messagebox
import time

# Sample text
sample_text = "CodeClause internship helps improve real-world coding skills."
start_time = 0

def start_typing():
    global start_time
    text_entry.delete("1.0", tk.END)
    result_label.config(text="")
    start_time = time.time()
    start_button.config(state="disabled")
    stop_button.config(state="normal")

def stop_typing():
    end_time = time.time()
    typed_text = text_entry.get("1.0", tk.END).strip()
    words_typed = len(typed_text.split())

    if typed_text == "":
        messagebox.showwarning("Warning", "You didn't type anything!")
        return

    time_taken = end_time - start_time
    wpm = round((words_typed / time_taken) * 60)
    result_label.config(text=f"Time: {round(time_taken, 2)} sec | WPM: {wpm}")

    start_button.config(state="normal")
    stop_button.config(state="disabled")

# GUI
root = tk.Tk()
root.title("Typing Speed Calculator")
root.geometry("600x400")
root.resizable(False, False)

tk.Label(root, text="Type this:", font=("Arial", 14)).pack(pady=10)
tk.Label(root, text=sample_text, font=("Arial", 12), wraplength=500, fg="blue").pack()

text_entry = tk.Text(root, height=6, width=60, font=("Arial", 12))
text_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()

start_button = tk.Button(button_frame, text="Start", command=start_typing, width=10)
start_button.grid(row=0, column=0, padx=10)

stop_button = tk.Button(button_frame, text="Stop", command=stop_typing, width=10, state="disabled")
stop_button.grid(row=0, column=1, padx=10)

result_label = tk.Label(root, text="", font=("Arial", 14), fg="green")
result_label.pack(pady=20)

root.mainloop()
