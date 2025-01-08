import math
import cmath

try:
    # Input values for the quadratic equation
    user_input1 = float(input("Enter the value of a: "))
    user_input2 = float(input("Enter the value of b: "))
    user_input3 = float(input("Enter the value of c: "))

    # Ensure 'a' is not zero to avoid division by zero
    if user_input1 == 0:
        print("The value of 'a' cannot be zero. This is not a quadratic equation.")
    else:
        # Calculate the discriminant
        discriminant = (user_input2 ** 2) - (4 * user_input1 * user_input3)

        # Check for different cases of the discriminant
        if discriminant > 0:  # Real and different roots
            # Integer square root for rationality check
            square_r = math.sqrt(discriminant)
            if square_r ** 2 == discriminant:  # Check if it's a perfect square
                solution1 = (-user_input2 - square_r) / (2 * user_input1)
                solution2 = (-user_input2 + square_r) / (2 * user_input1)
                print(
                    f"The solutions are {solution1} and {solution2}, they are real, different, and rational numbers.")
            else:
                solution1 = (-user_input2 - math.sqrt(discriminant)
                             ) / (2 * user_input1)
                solution2 = (-user_input2 + math.sqrt(discriminant)
                             ) / (2 * user_input1)
                print(
                    f"The solutions are {solution1} and {solution2}, they are real, different, and irrational numbers.")
        elif discriminant == 0:  # Real and same roots
            solution = -user_input2 / (2 * user_input1)
            print(
                f"The solution is {solution}, it is real, same, and rational.")
        else:  # Imaginary/non-real solutions
            solution1 = (-user_input2 - cmath.sqrt(discriminant)
                         ) / (2 * user_input1)
            solution2 = (-user_input2 + cmath.sqrt(discriminant)
                         ) / (2 * user_input1)
            print(
                f"The solutions are {solution1} and {solution2}, they are imaginary/non-real numbers.")

except ValueError:
    print("Please enter valid numbers.")

except Exception as e:
    print(f"An error occurred: {e}")
