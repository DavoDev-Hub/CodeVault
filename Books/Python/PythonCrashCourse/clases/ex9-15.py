'''
You can use a loop to see how hard it might be lo win the kind of lottery you just modeled. Make a list or tuple called my tidet. 
a loop that keeps pulling numbers until your ticket wins. Print a message reps ing how many times the loop had to run to give you a winning ticke!
'''
from random import choice
lottery = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E']
num1 = str(choice(lottery))
num2 = str(choice(lottery))
num3 = str(choice(lottery))
num4 = str(choice(lottery))
result = num1 + num2 + num3 + num4
print(result)
print("If any ticket matches these 4 numbers or letters, you win a prize!")

my_ticket = 'A2C4'
attempts = 0
while result != my_ticket:
    num1 = str(choice(lottery))
    num2 = str(choice(lottery))
    num3 = str(choice(lottery))
    num4 = str(choice(lottery))
    result = num1 + num2 + num3 + num4
    attempts += 1
print(f'Your ticket {my_ticket} won after {attempts} attempts! The winning combination was {result}.')

