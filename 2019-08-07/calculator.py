'''
Task: "Calculator"
Difficulty: Beginner
Description: Write a program that asks the user to enter a math problem, and then solves it for them.
In python, for example, there is a command called eval() which can take in a string (such as "2 * 40") and run it as if it
was written as a line of code in your program. You can combine this with input() (to get the math problem from the user)
and print() that we've looked at previously to make a calculator!
Bonus: Give your calculator some personality, is it a sassy calculator ("I can solve any problem your puny human brain
can devise!") or a reluctant calculator ("I don't think I can do this... did I do okay?") or something else?
'''

print("I am a *SuPeR* Calculator!")
print("Any SUM, big or small, is super easy!")
print("Let's give it a try, you give me a sum and I'll give you the answer.  Let's go!")
puzzle = input("What's your sum?: ")
print("Okay, got it")
print("Let me think about that for a second")
print("... carry the one ... square root ... brackets ...")
print("A-HA! The answer is", eval(puzzle))


'''
Comments: This should validate the user input, perhaps by only allowing certain characters. "eval"-ing the input without
checking is risky, I've done it here to make a simple program.
'''