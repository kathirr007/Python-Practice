def addition(num1, num2):
    return num1 + num2

def main():
    num1 = float(input('Enter your 1st Number: \n'))
    num2 = float(input('Enter your 2nd Number: \n'))

    result = addition(num1, num2)

    print('The result of the total is : ' + str(result))

main()