# This is a function declaration, named myCalc()
def myCalc():

#This store the operation you want to perfrom, maybe +, -, *
    operation = input('''
Please choose the calculation sign you want to perform:
+ This is the addition sign
- This is the subtraction sign
* This is the multiplication sign
/ This is the division sign
''')

#The number_1 and number_2 is a variable that store the first and second numbers the user enters

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

#The if, elif and else check for the operation the user choose, the else finally is trigger if none of the operation is choosen


    if operation == '+':
        print(number_1 + number_2)

    elif operation == '-':
        print(number_1 - number_2)

    elif operation == '*':
        print(number_1 * number_2)

    elif operation == '/':
        print(number_1 / number_2)

    else:
        print('Please ensure you enter the operation sign.')

# Call calculate() outside of the function
myCalc()