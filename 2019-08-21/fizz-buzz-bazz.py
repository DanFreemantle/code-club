'''
Task: "Fizz Buzz Bazz"
Difficulty: Intermediate
Description: 
Expand your "Fizz Buzz" program to print "Bazz" if the number is a multiple of 7.
For multiples of seven, print "Bazz" (instead of the number)
For multiples of three and seven, print "FizzBazz" (instead of the number)
For multiples of five and seven, print "BuzzBazz" (instead of the number)
For multiples of three, five and seven, print "FizzBuzzBazz" (instead of the number)
'''

for number in range(1, 101):
    result = ""

    if number % 3 == 0:
        result = result + "Fizz"

    if number % 5 == 0:
        result = result + "Buzz"

    if number % 7 == 0:
        result = result + "Bazz"

    if result == "":
        result = number
    
    print(result)