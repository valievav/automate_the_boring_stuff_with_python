'''
Write a function named collatz() that has one parameter named number.
If number is even, then collatz() should print number // 2 and return this value.
If number is odd, then collatz() should print and return 3 * number + 1.
'''

def collatz(number):
    count = 0
    while number != 1:
        count = count + 1
        if number % 2 == 0:
            number = number // 2
            print(number)
        else:
            number = 3 * number + 1
            print(number)
    print("Finished in " + str(count) + " tries")


# user value validation
try:
    number = int(input("Please enter a positive numeric value: \n"))
    if number <= 0:
        print("Negative values or 0 are not accepted. Please enter a positive numeric value.")
    else:
        collatz(number)
except ValueError:
    print("Non integer values are not accepted. Please enter a positive numeric value.")
