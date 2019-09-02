'''
Task: "Fizz Buzz"
Difficulty: Intermediate
Description: Write a program that prints the integers from 1 to 100 (inclusive)

But:
For multiples of three, print "Fizz" (instead of the number)
For multiples of five, print "Buzz" (instead of the number)
For multiples of both three and five, print "FizzBuzz" (instead of the number)

Expected output:
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
etc..
'''

for number in range(1, 101):
    if number % 5 == 0 and number % 3 == 0:
        print('FizzBuzz')
    elif number % 5 == 0:
        print ('Buzz')
    elif number % 3 == 0:
        print ('Fizz')
    else:
        print(number)