"""
Age on Other Planets Calculator
Author: Muhsin Ali Shah
License: This software is provided "as-is," without any express or implied warranty.
You are free to use, modify, and distribute this software with proper attribution to the author.
"""

import tkinter as tk
from tkinter import messagebox

# Orbital periods of planets relative to Earth (in Earth years)
orbital_periods = {
    "Mercury": 0.2408467,
    "Venus": 0.61519726,
    "Earth": 1.0,
    "Mars": 1.8808158,
    "Jupiter": 11.862615,
    "Saturn": 29.447498,
    "Uranus": 84.016846,
    "Neptune": 164.79132
}

# Function to calculate and display ages
def calculate_age():
    try:
        # Get the user's age on Earth
        earth_age = float(entry_age.get())
        if earth_age < 0:
            raise ValueError("Age cannot be negative.")
        
        # Calculate age on other planets
        result = "Your age on other planets:\n"
        for planet, period in orbital_periods.items():
            age_on_planet = earth_age / period
            result += f"{planet}: {age_on_planet:.2f} years\n"
        
        # Display the result in a message box
        messagebox.showinfo("Ages on Other Planets", result)
    except ValueError:
        # Handle invalid input
        messagebox.showerror("Input Error", "Please enter a valid positive number for your age.")

# Create the main window
root = tk.Tk()
root.title("Age on Other Planets Calculator")
root.geometry("400x300")
root.configure(bg="#f0f8ff")  # Light blue background color

# Add a header label
header_label = tk.Label(
    root,
    text="🌌 Age on Other Planets 🌍",
    font=("Arial", 16, "bold"),
    fg="#2a2a72",  # Dark blue text
    bg="#f0f8ff"   # Match background color
)
header_label.pack(pady=10)

# Instruction label
label_instruction = tk.Label(
    root,
    text="Enter your age on Earth (in years):",
    font=("Arial", 12),
    fg="#333333",  # Gray text
    bg="#f0f8ff"   # Match background color
)
label_instruction.pack(pady=10)

# Entry field for age
entry_age = tk.Entry(root, font=("Arial", 12), width=10, justify="center", bg="#ffffff", fg="#000000")
entry_age.pack(pady=5)

# Calculate button
button_calculate = tk.Button(
    root,
    text="Calculate",
    font=("Arial", 12, "bold"),
    bg="#007acc",  # Vibrant blue button
    fg="#ffffff",  # White text
    activebackground="#005f99",  # Darker blue on click
    activeforeground="#ffffff",  # White text on click
    command=calculate_age
)
button_calculate.pack(pady=10)

# Display author's name at the bottom
label_author = tk.Label(
    root,
    text="Developed by Muhsin Ali Shah",
    font=("Arial", 10, "italic"),
    fg="#555555",  # Subtle gray text
    bg="#f0f8ff"   # Match background color
)
label_author.pack(side="bottom", pady=10)

# Run the application
root.mainloop()
