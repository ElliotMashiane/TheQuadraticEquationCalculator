import tkinter as tk
import math
import cmath


def calculate_quadratic_equation():
    try:
        # Input values for the quadratic equation
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # Ensure 'a' is not zero to avoid division by zero
        if a == 0:
            result = "The value of 'a' cannot be zero. This is not a quadratic equation."
        else:
            # Calculate the discriminant
            discriminant = (b ** 2) - (4 * a * c)

            # Check for different cases of the discriminant
            if discriminant > 0:  # Real and different roots
                # Integer square root for rationality check
                square_r = math.sqrt(discriminant)
                if square_r ** 2 == discriminant:  # Check if it's a perfect square
                    solution1 = (-b - square_r) / (2 * a)
                    solution2 = (-b + square_r) / (2 * a)
                    result = (f"The solutions are {solution1} and {solution2}, "
                              f"they are real, different, and rational numbers.")
                else:
                    solution1 = (-b - math.sqrt(discriminant)) / (2 * a)
                    solution2 = (-b + math.sqrt(discriminant)) / (2 * a)
                    result = (f"The solutions are {solution1} and {solution2}, "
                              f"they are real, different, and irrational numbers.")
            elif discriminant == 0:  # Real and same roots
                solution = -b / (2 * a)
                result = (f"The solution is {solution}, "
                          f"it is real, same, and rational.")
            else:  # Imaginary/non-real solutions
                solution1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
                solution2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
                result = (f"The solutions are {solution1} and {solution2}, "
                          f"they are imaginary/non-real numbers.")

    except ValueError:
        result = "Please enter valid numbers."
    except Exception as e:
        result = f"An error occurred: {e}"

    # Display the result in the output text box
    output_text.delete("1.0", tk.END)  # Clear any previous output
    output_text.insert(tk.END, result)  # Insert the new result


def clear_inputs():
    # Clear all entry fields and output text
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    output_text.delete("1.0", tk.END)


# Create the GUI window
window = tk.Tk()
window.title("Quadratic Equation Solver")
window.geometry("500x400")
window.resizable(False, False)

# Create the GUI labels and textboxes for the quadratic equation coefficients
label_a = tk.Label(window, text="Enter the value of 'a':",
                   font=("Arial", 12, "bold"), padx=10, pady=10)
label_a.place(x=0, y=0)
entry_a = tk.Entry(window, font=("Arial", 12))
entry_a.place(x=200, y=10)

label_b = tk.Label(window, text="Enter the value of 'b':",
                   font=("Arial", 12, "bold"), padx=10, pady=10)
label_b.place(x=0, y=40)
entry_b = tk.Entry(window, font=("Arial", 12))
entry_b.place(x=200, y=50)

label_c = tk.Label(window, text="Enter the value of 'c':",
                   font=("Arial", 12, "bold"), padx=10, pady=10)
label_c.place(x=0, y=80)
entry_c = tk.Entry(window, font=("Arial", 12))
entry_c.place(x=200, y=90)

# The calculate BUTTON
calculate_button = tk.Button(window, text="Calculate", font=(
    "Arial", 12, "bold"), padx=10, pady=10, command=calculate_quadratic_equation)
calculate_button.place(x=200, y=130)

# Text widget for output
output_text = tk.Text(window, font=("Arial", 12),
                      height=5, width=50, bg="lightgrey")
output_text.place(x=22, y=200)

# The clear Button
clear_button = tk.Button(window, text="Clear", font=(
    "Arial", 12, "bold"), padx=10, pady=10, command=clear_inputs)
clear_button.place(x=220, y=300)

# Start of the GUI event loop
window.mainloop()
