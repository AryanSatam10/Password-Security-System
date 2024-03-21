import string
import random
import re
import tkinter as tk
from tkinter import messagebox
#GENERATING LIBERALS IN PASSWORD
def generate_password(plen):
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    password = "".join(random.sample(s, plen))
    return password
#CREATING PASSWORD LENGTH WITH EXCEPTIONS 
def check_password_strength(password):
    if len(password) < 8:
        return "Password must contain at least 8 characters."

    if not re.search("[A-Z]", password):
        return "Password must contain at least one uppercase letter."

    if not re.search("[a-z]", password):
        return "Password must contain at least one lowercase letter."

    if not re.search("[0-9]", password):
        return "Password must contain at least one digit."

    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."

    return "Password is strong."

def generate_and_check_password():
    plen = int(password_length_entry.get())
    password = generate_password(plen)
    generated_password_label.config(text="Generated Password: " + password)
    strength_message = check_password_strength(password)
    messagebox.showinfo("Password Strength", strength_message)

# GUI INTEGRATION 
root = tk.Tk()
root.title("Password Generator & Strength Checker")
password_length_label = tk.Label(root, text="Enter Password Length:")
password_length_label.pack()
password_length_entry = tk.Entry(root)
password_length_entry.pack()
generate_button = tk.Button(root, text="Generate Password", command=generate_and_check_password)  # Button to generate and check password
generate_button.pack()
generated_password_label = tk.Label(root, text="")  # Label to display generated password
generated_password_label.pack()
root.mainloop()

