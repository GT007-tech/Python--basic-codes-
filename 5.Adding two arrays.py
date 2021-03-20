from numpy import *
ite = int(input('Enter the number of elements in array 1 and 2:'))
c = []
b = []
for i in range(ite):

    c.insert(i,int(input("enter values of array 1 in integers/float ony:")))
arr1 = array(c)
print('array 1',arr1)
for i in range(ite):
    b.insert(i, int(input("enter values of array 2 in integers/float ony:")))
arr2 = array(b)
print('array 2',arr2)
d = zeros(ite)
for i in range(ite):
    d[i] = b[i] + c[i]
print('sum of two arrays =',d)
