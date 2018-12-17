number = int(input('Enter Your number: '))

def msg (number, text):
    print ('Your number {} {}'.format(number, text))

if  number% 4 == 0:
    msg(number, ' is a multiple of 4')
elif number% 2 == 0:
    msg(number, 'is even')
else:
    msg(number, 'is odd')

num = int(input("Pass the variable to be checked: "))
check = int(input("Pass the variable to divide by: "))

if num% check == 0:
    msg(num, 'divides evenly')
else:
    msg(num, 'do not split evenly.')