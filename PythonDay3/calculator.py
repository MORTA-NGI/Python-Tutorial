def sum(x,y):
    return x+y
def sub(x,y):
    return x-y
def div(x,y):
    return x/y
def multi(x,y):
    return x*y
while True:
    try:
        num1=int(input('Enter the first number 1:  '))
        num2=int(input('Enter the first number 2:  ')) 

        print('divition  is ', div(num1, num2))

    except ZeroDivisionError:
        print("ZeroDivisionError")
    except ValueError:
        print("ValueError")
