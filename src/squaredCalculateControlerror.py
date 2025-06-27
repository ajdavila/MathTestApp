import math

# Prompt the user to enter a number
number = float(input("Enter a number to calculate its square root: "))

# Calculate the square root
square_root = math.sqrt(number)

# Display the result with an explanation
print(f"The square root of {number} is {square_root}.")
print("We used the math.sqrt() function to compute the square root of the given number.")