import os

def main():
  program = input("Enter 1, 2, 3, or 4: ")
  while program not in ['1', '2', '3', '4']:
    os.system('clear')
    print("That's not a valid input.")
    program = input("Enter 1, 2, 3, or 4: ")

  os.system('clear')
  program = int(program)
  
  if program == 1:
    import part1
  elif program == 2:
    import part2
  elif program == 3:
    import part3
  elif program == 4:
    import part4

if __name__ == '__main__':
  main()