'''
Make a list or tuple containing a series of 10 numbers and 5 lete: Randomly select 4 
numbers or letters from the list and print a message saying fo any ticket matching these 4 
numbers or letters wins a prize
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