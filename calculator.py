
def addition(value1, value2):
      return value1 + value2


def subtraction(value1, value2):
      return value1 - value2


def multiply(value1, value2):
      return value1 * value2


def division(value1, value2):
      return value1 / value2


def saveToMemory():
      try:
            value = float(input('Enter Value to save: '))
            memory_file = open('memory.txt', 'w')
            memory_file.write(str(value))
            memory_file.close()
      except:
            print('Enter a valid value')


def RecallFromMemory():
      memory_file = open('memory.txt', 'r')
      memory_value = memory_file.read()

      return memory_value

def ClearMemory():
      memory_file = open('memory.txt', 'w')
      memory_file.write('none')

first_value = 'none'
second_value = 'none'
while True:

      print("OPERATIONS")
      print('1 ADD\n'
            '2 SUBTRACT\n'
            '3 MULTIPLY\n'
            '4 DIVIDE\n'
            '5 SAVE TO MEMORY\n'
            '6 RECALL FROM MEMORY\n'
            '7 CLEAR MEMORY\n'
            '8 EXIT')
      choice = input("Operation: ")

      if choice in ('1', '2', '3', '4'):
            try:
                  if first_value == 'none':
                        first_value = float(input('First Value: '))
                  else:
                        print('First value is', first_value)

                  if second_value == 'none':
                        second_value = float(input('Second Value: '))
                  else:
                        print('Second value is', second_value)

            except:
                  print('Enter a valid value')
                  print()
                  continue

            if choice == '1':
                  print(addition(first_value, second_value))
            elif choice == '2':
                  print(subtraction(first_value, second_value))
            elif choice == '3':
                  print(multiply(first_value, second_value))
            elif choice == '4':
                  print(division(first_value, second_value))

            first_value = 'none'
            second_value = 'none'

      elif choice == '5':
            saveToMemory()

      elif choice == '6':
            memory_value = RecallFromMemory()
            if memory_value == 'none':
                  print('Memory is empty')
            else:
                  while True:
                        print('Value in Memory: ', memory_value)
                        print('Select a operand to store the value from memory:\n'
                              '1 First operand\n'
                              '2 Second operand')
                        choice2 = input('Operand: ')
                        if choice2 == '1':
                              first_value = float(memory_value)
                              break
                        elif choice2 == '2':
                              second_value = float(memory_value)
                              break
                        else:
                              print("Select a valid choice")

      elif choice == '7':
            ClearMemory()
            first_value = 'none'
            second_value = 'none'
            print('Memory Cleared...')

      elif choice == '8':
            ClearMemory()
            print('Goodbye')
            exit()
      else:
            print("select a valid operation")


      print()