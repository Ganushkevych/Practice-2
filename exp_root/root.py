def root2(n):
    try:
        n = int(n)
        if n<0:
            raise ValueError
        return n ** (1/2)
    except ValueError:
        print("Введіть додатнє число")


def root3(n):
    try:
        n = int(n)
        return n ** (1/3)
    except ValueError:
        print("Введіть число")
