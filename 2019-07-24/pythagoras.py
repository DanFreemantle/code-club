'''
Task: "Pythagoras"
Difficulty: Intermediate
Description: Write a script that asks for the length of sides a and b of a right-angled triangle, then calculates and outputs the length of
side c (the hypotenuse)
The "power" symbol in most programming languages is ^ so writing "a squared" can also be written as a^2. Note that a*a
also works!
No labels
'''
import math

print("Pythagoras calculator.  Please enter the length of sides A and B on your right-angled triangle and I will calculate the length of side C (the hypotenuse)")
sideA = input("Enter the length of side A: ")
sideB = input("Enter the length of side B: ")

# Pythagoras = A^2 + B^2 = C^2
print("The length of the hypotenuse is", math.sqrt(int(sideA) ** 2 + int(sideB) ** 2))



'''
Comments: We're not checking user input, casting to an integer might fail.
'''