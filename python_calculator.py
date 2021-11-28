import math as m
def addition(a,b):
    x=a+b
    return x
def substraction(a,b):
    x=a-b
    return x
def multiplication(a,b):
    x=a*b
    return x
def division(a,b):
    x=a/b
    return x
def modulus(a,b):
    x=a%b
    return x
def square_root(a):
    x=m.sqrt(a)
    return x
def square(a):
    x=a*a
    return x

print('''
1.Addition operation.
2.substraction operation.
3.Multiplication operation.
4.Division Operation.
5.Modulus Operation.
6.square_root operation.
7.Square operation
''' )
option = eval(input('Please Select Any One Operation: '))
while option <= 7:
    if option == 1:
        n1 = eval(input('Enter First Number: '))
        n2 = eval(input('Enter Second Number: '))
        result = addition(n1,n2)
        print('The Addition of {} and {} is {}'.format(n1,n2,result))
    elif option == 2:
        n1 = eval(input('Enter First Number: '))
        n2 = eval(input('Enter Second Number: '))
        result = substraction(n1,n2)
        print("The Substraction of {} and {} is {}".format(n1,n2,result))
    elif option == 3:
        n1 = eval(input('Enter First Number: '))
        n2 = eval(input('Enter Second Number: '))
        result = multiplication(n1,n2)
        print("The Multiplication of {} and {} is {}".format(n1,n2,result))
    elif option == 4:
        n1 = eval(input('Enter First Number: '))
        n2 = eval(input('Enter Second Number: '))
        result = division(n1,n2)
        print("The Divivsion of {} and {} is {}".format(n1,n2,result))
    elif option == 5:
        n1 = eval(input('Enter First Number: '))
        n2 = eval(input('Enter Second Number: '))
        result = modudlus(n1,n2)
        print("The Modulus of {} and {} is {}".format(n1,n2,result))
    elif option == 6:
        n1 = eval(input('Enter Any Number: '))

        result = square_root(n1)
        print("The Square root of {} is {}".format(n1,result))
    elif option == 7:
        n1 = eval(input('Enter Any Number: '))

        result = square(n1)
        print("The Square of {} is {}".format(n1,result))
    else:
        print("Choose Correct Operation")

    choice = input("Do You Want to Perform Any Other Operation(Yes/NO): ")
    if choice == 'Yes':
        pass
        option = eval(input('Please Select Any One Operation: '))
    else:
        print("Thank You So Much")
        break
