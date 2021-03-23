def create_list():
    num = int(input("Enter the number of elements in your list"))
    l = []
    for i in range(num):
        c = input('Choose the type of element- i for integers, f for decimals and c for characters')
        if c == 'i':
            l.append(int(input('Enter the integer')))
        elif c == 'f':
            l.append(float(input("Enter the decimal number")))
        elif c == 'c':
            l.append(input('Enter the letter/word'))
        else:
            print('Enter i/c/f only as inputs')
            break
    return l

