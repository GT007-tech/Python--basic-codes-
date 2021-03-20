from array import *
ite = int(input('Enter the numbers of items in the array:'))
c=[]
for i in range(ite):

    c.insert(i,int(input("enter values of array in integers ony:")))
a = array('i',c)
print('The original array')
print(a)
c.sort()
asc = array('i',c)
print()
print('Array in ascending order')
print(asc)
c.reverse()
des = array('i',c)
print()
print("Array in descending order")
print(des)