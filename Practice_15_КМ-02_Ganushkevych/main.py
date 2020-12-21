from factorial.factorial import fact
from exp_root.exponentiation import exp2,exp3
from exp_root.root import root2,root3
from logarithm.logarithm import log,lg,ln
try:
    if __name__ == '__main__':
        f = input("Виберіть з нище вказаних функцій, ту що бажаєте використати\nФакторіал  -  f\nПіднесення до квадрату  -  2, до кубу  -  3\nЗнаходження корення квадратного  -  r2, кібучного  -  r3\nЛогарифма вибраного степеню  -  log, натурального  -  ln, десяткового  -  lg\n")
        if f =='f':
            print(fact(input("Введіть ціле додатнє число, від якого бажаєте знайти факторіал\t")))
        elif f =='2':
            print(exp2(input("Введіть число, квадрат якого бажаєте знайти\t")))
        elif f =='3':
            print(exp3(input("Введіть число, куб якого бажаєте знайти\t")))
        elif f =='r2':
            print(root2(input("Введіть число, корінь 2-го степеня якого бажаєте знайти\t")))
        elif f =='r3':
            print(root3(input("Введіть число, корінь 3-го степеня якого бажаєте знайти\t")))
        elif f =='log':
            print(log(input("Введіть числа:\nоснову логарифма\t"),input("та число\t")))
        elif f =='ln':
            print(ln(input("Введіть число\t")))
        elif f =='lg':
            print(lg(input("Введіть число\t")))
        else:
            print("Такої функції не задано")
except NameError and ValueError:
    print("Введіть правильні значення")



