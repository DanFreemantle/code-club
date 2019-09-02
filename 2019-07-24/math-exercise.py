'''
Task: "Math!"
Difficulty: Beginner
Description: Write a program that will output the answers to the following math problems:
98234 + 2004
75250 - 9441
61 * 22 (note most programming languages use * as the multiply symbol)
500 / 40
'''

problems = ["98234 + 2004", "75250 - 9441", "61 * 22", "500 / 40"]
for problem in problems:
    print (problem, "=", eval(problem))