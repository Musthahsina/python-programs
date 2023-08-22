import string
import secrets
import tkinter as tk
from tkinter import ttk, messagebox


def generate_password(length=12, include_lowercase=True, include_uppercase=True, include_digits=True,
                      include_symbols=True):
    characters = ''
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be included.")

    if length < 8:
        messagebox.showwarning("Weak Password",
                               "Password length is too short. It is recommended to use at least 8 characters.")

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password


def generate_and_show_password():
    password_length = int(length_var.get())
    include_lowercase = lowercase_var.get()
    include_uppercase = uppercase_var.get()
    include_digits = digits_var.get()
    include_symbols = symbols_var.get()

    try:
        generated_password = generate_password(
            length=password_length,
            include_lowercase=include_lowercase,
            include_uppercase=include_uppercase,
            include_digits=include_digits,
            include_symbols=include_symbols
        )
        password_var.set(generated_password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))


# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")

# Password Length
length_label = ttk.Label(root, text="Password Length:")
length_label.pack()
length_var = tk.StringVar(value="12")
length_entry = ttk.Entry(root, textvariable=length_var)
length_entry.pack()

# Character Options
lowercase_var = tk.BooleanVar(value=True)
uppercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

lowercase_cb = ttk.Checkbutton(root, text="Lowercase", variable=lowercase_var)
uppercase_cb = ttk.Checkbutton(root, text="Uppercase", variable=uppercase_var)
digits_cb = ttk.Checkbutton(root, text="Digits", variable=digits_var)
symbols_cb = ttk.Checkbutton(root, text="Symbols", variable=symbols_var)

lowercase_cb.pack()
uppercase_cb.pack()
digits_cb.pack()
symbols_cb.pack()

# Generate Button
generate_button = ttk.Button(root, text="Generate Password", command=generate_and_show_password)
generate_button.pack()

# Generated Password Display
password_var = tk.StringVar(value="")
password_label = ttk.Label(root, text="Generated Password:")
password_label.pack()
password_entry = ttk.Entry(root, textvariable=password_var, state="readonly")
password_entry.pack()

root.mainloop()
