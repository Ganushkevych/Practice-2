def fact(n):
    try:
        n = int(n)
        if n<0:
            raise ValueError
        elif n==0:
            return 1
        if n==1:
            return 1
        else:
            r= n*fact(n-1)
            return r
    except ValueError:
        print("Введіть натуральне число")

