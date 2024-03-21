import tkinter as tk

# Function to encrypt plaintext using Affine Cipher
def affine_cipher_encrypt(plaintext, a, b):
    # Remove spaces from the plaintext
    plaintext = plaintext.replace(" ", "")
    
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():  # Check if the character is alphabetic
            if char.islower():
                x = ord(char) - ord('a')  # Convert character to its numeric equivalent (0-indexed)
                encrypted_char = chr(((a * x + b) % 26) + ord('a'))  # Apply the encryption function
            elif char.isupper():
                x = ord(char) - ord('A')  # Convert character to its numeric equivalent (0-indexed)
                encrypted_char = chr(((a * x + b) % 26) + ord('A'))  # Apply the encryption function
        else:
            encrypted_char = char  # Keep non-alphabetic characters unchanged
        ciphertext += encrypted_char
    return ciphertext

# Function to handle button click event
def encrypt_button_click():
    plaintext = plaintext_entry.get()  # Get the plaintext from the entry widget
    a = int(a_entry.get())  # Get the 'a' key from the entry widget
    b = int(b_entry.get())  # Get the 'b' key from the entry widget
    ciphertext = affine_cipher_encrypt(plaintext, a, b)  # Encrypt the plaintext
    ciphertext_label.config(text="Ciphertext: " + ciphertext)  # Update the ciphertext label

# Create the main window
root = tk.Tk()
root.title("Affine Cipher Encryption")
root.geometry("400x250")  # Width x Height

# Widgets for entering plaintext, keys, and displaying ciphertext
plaintext_label = tk.Label(root, text="Enter Plain Text:")
plaintext_label.pack()

plaintext_entry = tk.Entry(root, width=40)
plaintext_entry.pack()

a_label = tk.Label(root, text="Enter 'a' Key (1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25):")
a_label.pack()

a_entry = tk.Entry(root, width=10)
a_entry.pack()

b_label = tk.Label(root, text="Enter 'b' Key:")
b_label.pack()

b_entry = tk.Entry(root, width=10)
b_entry.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_button_click)
encrypt_button.pack()

ciphertext_label = tk.Label(root, text="Ciphertext: ")
ciphertext_label.pack()

# Start the main loop
root.mainloop()  # This loop keeps the window running and responsive
