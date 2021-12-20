"""
******
PART 1
******
The program below is supposed to ask the user to enter an integer input, and print the product of all of the positive integers less than or equal to that number (also known as the factorial of the number). For example, if the user enter 5, the program should print 120 (since 5! = 5*4*3*2*1 = 120).

The program doesn't work quite right yet, though. Fix the program so that it runs the way it should (there should be at 3 things you need to change.)
"""

number = int(input("What factorial are you looking for? "))

product = 0

for i in range(number):
  product = product * i

print(product)