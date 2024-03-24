import tkinter as tk
import numpy as np

def hill_cipher_encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    n = len(key)
    plaintext += 'X' * (n - len(plaintext) % n)
    ciphertext = ''
    for i in range(0, len(plaintext), n):
        chunk = [ord(char) - ord('A') for char in plaintext[i:i+n]]
        chunk = np.array(chunk)
        encrypted_chunk = np.dot(key, chunk) % 26
        for num in encrypted_chunk:
            ciphertext += chr(num + ord('A'))
    return ciphertext

def encrypt_button_click():
    plaintext = plaintext_entry.get()
    key_str = key_entry.get()
    key = np.fromstring(key_str, dtype=int, sep=',').reshape((3, 3))
    ciphertext = hill_cipher_encrypt(plaintext, key)
    ciphertext_label.config(text="Ciphertext: " + ciphertext)

# Create the main window
window = tk.Tk()
window.title("Hill Cipher Encryption")
window.geometry("500x200")  # W x H ;)

plaintext_label = tk.Label(window, text="Enter Plaintext:")
plaintext_label.pack()

plaintext_entry = tk.Entry(window, width=40)
plaintext_entry.pack()

key_label = tk.Label(window, text="Enter Key (9 numbers separated by commas):")
key_label.pack()

key_entry = tk.Entry(window, width=40)
key_entry.pack()

encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_button_click)
encrypt_button.pack()

ciphertext_label = tk.Label(window, text="")
ciphertext_label.pack()

# Starter the main loop
window.mainloop()