from numpy import *
order = []
c=[]
d=[]
order.insert(0,int(input('Enter the number of rows in matrix 1:')))
order.insert(1,int(input('Enter the number of columns in matrix 1:')))
order.insert(2,int(input('Enter the number of rows in matrix 2:')))
order.insert(3,int(input('Enter the number of columns in matrix 2:')))
################################################
if order[2] == order[1]:
    type = input("select matrix 1 elements type: 'f' for float and 'i' for int:")
    if type == 'i':
        for i in range(order[0]*order[1]):
            c.insert(i, int(input("enter values of matrix 1 in integers only:")))
    elif type == 'f':
        for i in range(order[0]*order[1]):
            c.insert(i, float(input("enter values of matrix 1 in float only:")))
    else:
        print("please type either i or f")
    mar1 = array(c)
    mar1 = mar1.reshape(order[0],order[1])
    mar1 = matrix(mar1)
    print("Matrix 1:",mar1)
    ######################################################
    type = input("select  matrix 2 elements type: 'f' for float and 'i' for int:")
    if type == 'i':
        for i in range(order[2]*order[3]):
            d.insert(i, int(input("enter values of matrix 2 in integers only:")))  # creates an array as input
    elif type == 'f':
        for i in range(order[2]*order[3]):
            d.insert(i, float(input("enter values of matrix 2 in float only:")))  # creates an array as input
    else:
        print("please type either i or f")
    mar2 = array(d)
    mar2 = mar2.reshape(order[2],order[3])
    mar2 = matrix(mar2)
    print("Matrix 2:",mar2)
    ################################
    mar3 = zeros(order[0]*order[3])
    mar3 = mar3.reshape(order[0],order[3])
    for i in range(order[3]):
        for j in range(order[0]):
            mar3[i, j] = sum(mar1[i, :] * mar2[:, j])
    print(mar3)
else:
    print('Enter orders of two matrices such that, number of columns of matrix1 is same as number of rows of matrix2')

print('END!')
