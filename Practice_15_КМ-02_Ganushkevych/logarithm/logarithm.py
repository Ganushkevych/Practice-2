def log(a,b):
    try:
        a = float(a)
        b = float(b)
        if a<0 or a==1 or b<0:
            raise ValueError
        round(a,1)
        s = -10
        while b!=round(a**s,1):
            s = round(s + 0.01,3)
        return s
    except ValueError and OverflowError:
        print("Введіть а більше за 0 і не 1 та b більше за 0, такі щоб хоча б приблизно обчислювався логарифм")


def lg(b):
    try:
        b = round(float(b),2)
        if b<0:
            raise ValueError
        s = -10
        a = 10
        while b!=round(a**s,2):
            s = round(s + 0.01,2)
        return round(s)
    except ValueError and OverflowError:
        print("Введіть b більше за 0, таке щоб хоча б приблизно обчислювався логарифм")


def ln(b):
    import math
    try:
        b = round(float(b),1)
        if b<0:
            raise ValueError
        s = -10
        a = math.e
        while b!=round(a**s,1):
            s = round(s + 0.1,1)
        return s
    except ValueError and OverflowError:
        print("Введіть b більше за 0, таке щоб хоча б приблизно обчислювався логарифм")