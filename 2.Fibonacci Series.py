num = int(input("Enter the highest term you want to know"))
i = 1
m = 2
n = 0
if num <= 0:
    print("enter positive number only")
elif num == 1:
    print(0)
else:
    print('The following are first',num,'terms of Fibonacci Series')
    print(0)
    while m<= num:
        j = i + n
        i = n
        n = j
        print(j)
        m+=1
print('END')
