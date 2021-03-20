from math import sqrt
n = int(input('Enter the number to check whether it is prime or not'))
if n>1:
    for i in range(2,int(sqrt(n+1)),1):
        if n%i == 0:
            print("Not a prime number")
            break
    else:
        print(n,'is a prime number')
else:
    print('Please enter positive integer greater than 1')

print('END!')
