import cmath

user_input1 = float(input("Enter the value of a: "))
user_input2 = float(input("Enter the value of b: "))
user_input3 = float(input("Enter the value of c: "))

# Calculate the discriminant
discriminant = (user_input2**2) - (4*user_input1*user_input3)

# Find two solutions
solution1 = (-user_input2-cmath.sqrt(discriminant))/(2*user_input1)
solution2 = (-user_input2+cmath.sqrt(discriminant))/(2*user_input1)

print(f"The solutions are {solution1} and {solution2}")
