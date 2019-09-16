'''
Task: "A square loop"
Difficulty: Intermediate
Description: Write a program that asks the user to input an integer between 2 and 20.
Output every number squared up to and including the number they entered. Each square should be on a separate line.
For instance, if the user enters "5" the expected output will be the numbers 0, 1, 2, 3, 4 and 5 squared:
0
1
4
9
16
25
'''
square = input("Please enter an integer between 2 and 20: ")

try:
    maximum = int(square)

    if maximum < 2 or maximum > 20:
        raise ValueError()

    for i in range(0, maximum + 1):
        print(i * i)

except ValueError:
    print("Please enter a valid number in the range 2 to 20")