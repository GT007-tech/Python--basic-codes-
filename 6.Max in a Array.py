from numpy import *
ite = int(input('Enter the length of array:'))
type = input("select array tpe: 'f' for float and 'i' for int")
c = []
if type == 'i':
    for i in range(ite):
        c.insert(i,int(input("enter values of array in integers/float ony:"))) # creates an array as input
elif type == 'f':
    for i in range(ite):
        c.insert(i,float(input("enter values of array in integers/float ony:"))) # creates an array as input
else:
    print("please type either i or f")
a = array(c)
print('array:',a)
for j in range(ite-1):
    for i in range(ite-1):
        if a[i] < a[i+1]:
            a[i], a[i + 1] = a[i + 1], a[i]
        else:
            pass
print(a)
print('max. element', a[0])
