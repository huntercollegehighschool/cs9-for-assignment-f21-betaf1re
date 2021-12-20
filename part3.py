"""
******
PART 3
******

Write a program that prompts the user to enter two integers, one representing the base of a rectangle, and one representing the height. The program will then print a rectangle made of asterisks (*) with those dimensions. 

(Hint: this may involve nested for loops(ie. a for loop inside a for loop), but it does not have to. Concatenating/adding strings ('*' + '*') or replicating strings ('*' * 3) may be helpful here.)

An example of what should appear on the console when the program runs:

Enter the base: 7
Enter the height: 3

*******
*******
*******

"""

#write your code here 
length = int(input("Enter the length: "))
width = int(input("Enter the width: "))
print("\n")

base = ""
side = ""

for n in range(length):
  base += '*'
  if n == 0 or n == length-1:
    side += '*'
  else:
    side += ' '

for n in range(width):
  if n == 0 or n == width-1:
    print(base)
  else:
    print(side)

print('\n')

#i didn't realize that you could just make a filled rectangle are you kidding me aaaa
line = ""
for n in range(length):
  line += '*'
for n in range(width):
  print(line)