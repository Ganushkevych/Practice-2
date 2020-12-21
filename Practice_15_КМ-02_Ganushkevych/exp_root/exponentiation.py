def exp2(n):
    try:
        n=float(n)
        return n**2
    except ValueError:
        print("Введіть число")


def exp3(n):
    try:
        n=float(n)
        return n**3
    except ValueError:
        print("Введіть число")
