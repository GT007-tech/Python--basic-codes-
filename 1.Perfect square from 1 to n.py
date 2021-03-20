from math import sqrt,floor # to import specific methods from a module
n = int(input('please enter the number upto which you want to find the perfect squares:'))
print("the following are perfect squares from 1 to", n)
for i in range(1,n+1,1):
    if sqrt(i) == floor(sqrt(i)):
        print(i,",",end='' )
