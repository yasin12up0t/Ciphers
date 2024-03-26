import tkinter as tk
from tkinter import messagebox

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def calculate_y():
    try:
        x_value = int(entry.get())
        y_value = mod_inverse(x_value, 26)
        result_label.config(text=f"The value of y is: {y_value}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer")

root = tk.Tk()
root.title("Modular Inverse Calculator")
entry_label = tk.Label(root, text="Enter the x value:")
entry_label.pack()
entry = tk.Entry(root)
entry.pack()
calculate_button = tk.Button(root, text="Calculate", command=calculate_y)
calculate_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()