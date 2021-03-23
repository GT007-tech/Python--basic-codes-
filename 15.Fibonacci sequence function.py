def fib(n):
    i = 1
    m = 0
    if n > 0:
        if n == 1:
            print(0)
        else:
            if n == int(n):
                print(0)
                for k in range(1, n):
                    j = i + m
                    i = m
                    m = j
                    print(j)
            else:
                print('The entered argument has to be an integer only')
    else:
        print("Enter positive integers only")

#Enter a number
fib(10)