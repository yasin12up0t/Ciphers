import tkinter as tk

def rail_fence_cipher_encrypt(plaintext, num_rows):
    
    plaintext = plaintext.replace(" ", "")
    # Initialize an empty matrix for Rail Fence Cipher
    rail_fence = []
    for _ in range(num_rows):
        rail_fence.append([''] * len(plaintext))

    # Fill the rail fence matrix
    row = 0
    down = True
    for i in range(len(plaintext)):
        rail_fence[row][i] = plaintext[i]

        # Move down or up depending on the direction
        if row == num_rows - 1:  # Check if the cursor has reached the bottom row of the matrix
            down = False  # If it has, change the direction to up (set down to False)
        elif row == 0:  # Check if the cursor has reached the top row of the matrix
            down = True  # If it has, change the direction to down (set down to True)
        if down:
            row += 1  # If the direction is down, move the cursor to the next row downwards
        else:
            row -= 1  # If the direction is up, move the cursor to the next row upwards
    
    # Read off the rail fence matrix to get ciphertext
    ciphertext = ''
    for i in range(num_rows):
        ciphertext += ''.join(rail_fence[i])
    
    return ciphertext

# Function to handle button click event
def encrypt_button_click():
    plaintext = plaintext_entry.get()  # Get the plaintext from the entry widget
    num_rows = int(num_rows_entry.get())  # Get the number of rows from the entry widget
    ciphertext = rail_fence_cipher_encrypt(plaintext, num_rows)  # Encrypt the plaintext
    ciphertext_label.config(text="Ciphertext: " + ciphertext)  # Update the ciphertext label

# Create the main window
root = tk.Tk()
root.title("Rail Fence Cipher Encryption")
root.geometry("400x200")  # W x H
plaintext_label = tk.Label(root, text="Enter Plain Text:")
plaintext_label.pack()
plaintext_entry = tk.Entry(root, width=40)
plaintext_entry.pack()
num_rows_label = tk.Label(root, text="Enter Number of Rows:")
num_rows_label.pack()
num_rows_entry = tk.Entry(root, width=10)
num_rows_entry.pack()
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_button_click)
encrypt_button.pack()
ciphertext_label = tk.Label(root, text="Ciphertext: ")
ciphertext_label.pack()

# Start the main loop
root.mainloop()  # This loop keeps the window running and responsive
