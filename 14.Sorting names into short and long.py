def names_sort():
    num = int(input("Enter the number of names you want to sort"))
    names = []
    s = []
    l = []
    j,k = 0,0
    for i in range(num):
        names.append(input('Enter the name you want to sort'))
    for i in range(num):
        if len(names[i]) <= 5:
            s.append(names[i])
            j+=1

        else:
            l.append(names[i])
            k+=1


    print("Short names: {}".format(s))
    print("Long names: {}".format(l))


names_sort()
