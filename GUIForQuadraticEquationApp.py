import tkinter as tk

# Create the GUI window
window = tk.Tk()

# Set the title of the GUI window
window.title("Quadratic Equation Solver")

# Create the GUI size window
window.geometry("500x600")

# Make the GUI window non-resizable
window.resizable(False, False)

# Create the GUI labels and textboxes for the quadratic equation coefficients
label_a = tk.Label(window, text="Enter the value of 'a': ",
                   font=("Arial", 12, "bold"), padx=10, pady=10)
label_a.place(x=0, y=0)
entry_a = tk.Entry(window, font=("Arial", 12))
entry_a.place(x=200, y=10)

label_b = tk.Label(window, text="Enter the value of 'b': ",
                   font=("Arial", 12, "bold"), padx=10, pady=10)
label_b.place(x=0, y=40)
entry_b = tk.Entry(window, font=("Arial", 12))
entry_b.place(x=200, y=50)

label_c = tk.Label(window, text="Enter the value of 'c': ",
                   font=("Arial", 12, "bold"), padx=10, pady=10)
label_c.place(x=0, y=80)
entry_c = tk.Entry(window, font=("Arial", 12))
entry_c.place(x=200, y=90)


# The calculate BUTTON
button = tk.Button(window, text="Calculate", font=(
    "Arial", 12, "bold"), padx=10, pady=10)
button.place(x=200, y=130)

# Start of the GUI event loop
window.mainloop()
