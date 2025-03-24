import tkinter as tk
import math

# Function to handle button clicks
def on_button_click(value):
    entry.insert(tk.END, value)

# Function to evaluate the entered expression
def evaluate_expression():
    try:
        expression = entry.get()
        # Replace advanced functions with their math equivalents
        expression = expression.replace("sin", "math.sin")
        expression = expression.replace("cos", "math.cos")
        expression = expression.replace("tan", "math.tan")
        expression = expression.replace("log", "math.log")
        expression = expression.replace("exp", "math.exp")
        result = eval(expression)  # Use eval carefully
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Function to toggle themes
def toggle_theme():
    if root['bg'] == "white":
        root['bg'] = "black"
        entry['bg'] = "black"
        entry['fg'] = "white"
        theme_button['bg'] = "#555"
        theme_button['fg'] = "white"
        for button in all_buttons:
            button['bg'] = "#333"
            button['fg'] = "white"
    else:
        root['bg'] = "white"
        entry['bg'] = "white"
        entry['fg'] = "black"
        theme_button['bg'] = "#ddd"
        theme_button['fg'] = "black"
        for button in all_buttons:
            button['bg'] = "#f0f0f0"
            button['fg'] = "black"

# Create main window
root = tk.Tk()
root.title("Lahari Calculator")
root.geometry("400x500")
root.configure(bg="white")

# Entry field for displaying input/output
entry = tk.Entry(root, font=("Arial", 20), justify="right", bd=10, relief=tk.RIDGE)
entry.pack(pady=10, padx=10, fill=tk.BOTH)

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('sin', 'cos', 'tan', 'log'),
    ('C', '0', '=', '+')
]

# Button frame
button_frame = tk.Frame(root, bg="white")
button_frame.pack()

# Generate buttons dynamically
all_buttons = []
for row in buttons:
    button_row = tk.Frame(button_frame, bg="white")
    button_row.pack()
    for char in row:
        btn = tk.Button(
            button_row, text=char, font=("Arial", 16),
            width=5, height=2, bg="#f0f0f0", fg="#333",
            activebackground="#add8e6", activeforeground="#000",
            command=lambda c=char: on_button_click(c) if c not in ("=", "C") else (evaluate_expression() if c == "=" else clear_entry())
        )
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Enter>", lambda e, b=btn: b.configure(bg="#d3d3d3"))
        btn.bind("<Leave>", lambda e, b=btn: b.configure(bg="#f0f0f0"))
        all_buttons.append(btn)

# Theme toggle button
theme_button = tk.Button(
    root, text="Toggle Theme", font=("Arial", 12),
    bg="#ddd", fg="black", command=toggle_theme
)
theme_button.pack(pady=10)

# Run the application
root.mainloop()
