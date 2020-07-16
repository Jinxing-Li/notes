main = input("I'm thinking of a number! Try to guess the number I'm thinking of ")
print('\n\n\n\n\n\n\n\n\n\n\n')


for i in range(100):
     value = input('Please start guessing!!!')
     if int(main) > int(value):
          value = print('TOO LOW! try again
     
     elif int(main) < int(value):
          value = print('TOO HIGH! try again!')
     else:
          print('Wow, Good, excellent!')
          break
     del value