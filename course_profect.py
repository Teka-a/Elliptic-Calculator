import dots
import equation
from tabulate import tabulate
from matplotlib import pyplot as plt

print("Для шифрования необходимо выбрать модуль - простое число, больше 48")
print("Уравнение: ")
print("     Ep(a,b): y^2 ≡ x^3 + a x + b")

a = int(input("Введите а: "))
b = int(input("Введите b: "))
p = int(input("Введите p: "))

wish = input("Нужны подробности решения? (y/n): ")
dots.wish = wish
equation.wish = wish

group_of_dots = []
last = []
goods = []
dots_x = []
dots_y = []
alphabet = ['!', ',', '.', '?', 'а', 'б', 'в', 'г', 'д', 'е', 'ё','ж', 'з', 'и', 'й', ' к', 'л', 'м', 'н', 'о', 'п', 'р',
	'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ', '0', '1', '2', '3', '4', '5', '6',
    '7', '8', '9']
"""
print(len(alphabet))
q = 0
a = 1
b = 3
p = 7
"""

def fill_x_y (dots):
    for i in dots:
        dots_x.append(i[0])
        dots_y.append(i[1])


def lasts(row):
    if(['not'] in row):
        ind = row.index(['not'])
        last.append([row[ind-1], ind])


def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True


def double_dot (x1, y1, mod, a):
    equation.print_if_need("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    equation.print_if_need(f"Удвоение точки: ({x1}, {y1}) mod = {mod} a = {a}")
    if (y1 != 0):
        lamup = (3 * (x1 ** 2)) + a
        lamdown = 2 * y1
        lam = equation.eq(lamdown, lamup, mod)
        x3 = (lam ** 2 - 2 * x1) % mod
        y3 = (lam * (x1 - x3) - y1) % mod
        equation.print_if_need(f"λ = (3*x1^2 + a) / (2*y1) = (3*{x1}^2 + {a}) / (2*{y1}) = {lam} (mod {mod})")
        equation.print_if_need(f"x3 = λ^2 - 2*x1 = {lam}^2 - 2*{x1} = {x3} (mod {mod})")
        equation.print_if_need(f"y3 = λ * (x1 - x3) - y1 = {lam} * ({x1} - {x3}) - {y1} = {y3} (mod {mod})")
        equation.print_if_need(f"2P = (x3, y3) -> 2*({x1}, {y1}) = ({x3}, {y3})")
        return [x3, y3]
    else:
        return ["not"]


def sum_dots (x1, y1, x2, y2, mod):
    equation.print_if_need("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    equation.print_if_need(f"Сложение точек: ({x1}, {y1}) и ({x2}, {y2}) mod = {mod}")
    if ((x2 - x1) != 0):
        lamup = y2 - y1
        lamdown = x2 - x1
        lam = equation.eq(lamdown, lamup, p)
        x3 = (lam ** 2 - x1 - x2) % mod
        y3 = (lam * (x1 - x3) - y1) % mod
        equation.print_if_need(f"λ = (y2 - y1) / (x2 - x1) = ({y2} - {y1}) / ({x2} - {x1}) = {lam} (mod {mod})")
        equation.print_if_need(f"x3 = λ^2 - x1 - x2 = {lam}^2 - {x1} - {x2} = {x3} (mod {mod})")
        equation.print_if_need(f"y3 = λ * (x1 - x3) - y1 = {lam} * ({x1} - {x3}) - {y1} = {y3} (mod {mod})")
        equation.print_if_need(f"P + Q = R -> ({x1}, {y1}) + ({x2}, {y2}) = ({x3}, {y3})")
        return [x3, y3]
    else:
        return ["not"]


def count_compositions(k, P, p, a):
    for i in range(2, k):
        if (i % 2 == 0):
            # 2*P[i//2]
            # P[i] = doubleDot(P[i//2][0], P[i//2][1], mod, a)
            if (P[i // 2] == ['not']):
                P[i] = P[i // 2]
                # print("u")
            else:
                # print(P[i//2][0], P[i//2][1])
                P[i] = double_dot(P[i // 2][0], P[i // 2][1], p, a)
            # print("even", P[i])
        else:
            # P[1]+P[i-1]  doubleDot(P[1][0], P[1][1], mod, a)
            if (P[1][0] != P[i - 1][0]):
                if (P[i - 1] == ['not']):
                    P[i] = P[1]
                    # print("o")
                else:
                    P[i] = sum_dots(P[1][0], P[1][1], P[i - 1][0], P[i - 1][1], p)
            elif ((P[1][0] == P[i - 1][0]) and (P[1][1] == (-P[i - 1][1]) % p)):
                P[i] = ['not']
                # print("h")
            else:
                P[i] = double_dot(P[1][0], P[1][1], p, a)
            # print("not even", P[i])
    return P


def map_of_dots (a, p, group_of_dots):
    table = [[0]] * len(group_of_dots)
    for i in range(len(table)):
        table[i] = [0] * p
        table[i][1] = group_of_dots[i]

    for P in table:
        count_compositions(p, P, p, a)

    # print_table(table, mod)
    for u in table:
        lasts(u)

    for t in last:
        n = t[1]
        if n <= 2:
            continue
        if (is_prime(n)):
            goods.append(t)

    new_data = []
    mas = []
    for t in range(1, p):
        mas.append(t)
    new_data.append(mas)
    for i in table:
        i.remove(0)
        line = []
        for p in i:
            if (p != ['not']):
                line.append("(" + str(p[0]) + ", " + str(p[1]) + ")")
            else:
                line.append("O")
        new_data.append(line)
    qs = []
    for l in goods:
        qs.append(l[1])
    print("Table:")
    print(tabulate(new_data))
    print("Last dots: ", last)
    print("Suitable dots:", goods)
    return max(qs)


def find_composition(dot_x, dot_y, k, a, p):
    num = k+1
    line_of_comp = [[0]] * (num)
    line_of_comp[1] = [dot_x, dot_y]
    compositions = count_compositions(num, line_of_comp, p, a)
    return compositions.pop()


def visual_presentation (a, b, p):
    group_of_dots = dots.find_dots(a, b, p)
    fill_x_y(group_of_dots)
    plt.scatter(dots_x, dots_y)



print("Ваше уравнение: E" + str(p) + "(" + str(a) + "," + str(b) + "): y^2 ≡ x^3 +", a, "x +", b, "mod", p)

if (p == 2 or p == 3):
    print("Извините, калькулятор предназначен пока что только для рассчетов по канонической форме Вейерштрасса(")
    raise SystemExit

check = ((4*(a**3)) + (27*(b**2))) % p
c_up_a = a**3
c_down_a = 3**3
c_up_b = b**2
c_down_b = 2**2
up = equation.eq(c_down_a, c_up_a, p)
down = equation.eq(c_down_b, c_up_b, p)
print(c_up_a)
print(c_up_b)
print(up+down)
if (check==0):
    print("Это особая кривая! Она не представляет интереса для криптографии(")
    raise SystemExit
invariant = ((1728*4*(a**3))//(4*(a**3) + 27*(b**2)))%p
invariant = ((1728*4*(a**3))//(4*(a**3) + 27*(b**2)))%p

print(f"\nДельта = 4a^3 + 27b^2 (mod p) = {check} (mod {p}) ≠ 0")
print(f"\nИнвариант = (1728*4*(a**3))/(4a^3 + 27b^2) (mod p) = {invariant} ")
while True:
    print("1. Найти композицию точки на эллиптической кривой.")
    print("2. Найти точки и построить карту точек эллиптической кривой, определить порядок кривой + построить график расположения точек эллиптической кривой.")
    print("3. Графически представить сложение подходящих точек.")
    print("4. ЕСС с использованием абсциссы точки. (Сначала обязательно воспользоваться 2 пунктом)")
    print("0. Выйти из программы")
    cmd = input("Выберите пункт: ")

    if cmd == "1":
        k = int(input("Введите k: "))
        x = int(input("Введите x: "))
        y = int(input("Введите y: "))
        k_composition = find_composition(x, y, k, a, p)
        print(f"[k](x, y) = [{k}]({x}, {y}) = ({k_composition[0]}, {k_composition[1]})")
    elif cmd == "2":
        group_of_dots = dots.find_dots(a, b, p)
        print(group_of_dots)
        q = map_of_dots(a, p, group_of_dots)
        print("Порядок кривой:", q)
        visual_presentation(a, b, p)
        plt.show()
    elif cmd == "3":
        visual_presentation(a, b, p)
        print(goods)
        x1 = int(input("Введите x1: "))
        y1 = int(input("Введите y1: "))
        x2 = int(input("Введите x2: "))
        y2 = int(input("Введите y2: "))
        third_dot = sum_dots(x1, y1, x2, y2, p)
        if group_of_dots == []:
            group_of_dots = dots.find_dots(a, b, p)
        x3, y3, x4, y4 = third_dot[0], third_dot[1], 0, 0
        if third_dot == "not":
            print("not")
            break
        for i in group_of_dots:
            if (i[0] == x3 and i[1] != y3):
                x4 = i[0]
                y4 = i[1]
        plt.plot([x1, x2, x4], [y1, y2, y4])
        plt.plot([x3, x4], [y3, y4])
        plt.text(x1 - 0.25, y1, "P")
        plt.text(x2 + 0.25, y2, "Q")
        plt.text(x3, y3, "R")
        plt.text(x4 + 0.15, y4, "R'")
        plt.show()
    elif cmd == "4":
        secret_key = 0
        R = []
        sipher = []
        if (p < 48 or not is_prime(p)):
            print("Выберите простой модуль больше 48!")
        else:
            print("Выберите точку G: ", goods)
            x1 = int(input("Введите x1: "))
            y1 = int(input("Введите y1: "))
            if ([[x1, y1], q] in goods):
                print("Выберите секретный ключ: 0 < key < q (порядок точки). Порядок точки для данной кривой: ", q)
                secret_key = int(input("Введите секретный ключ: "))
                if (secret_key > 0 and secret_key < q):
                    open_key = find_composition(x1, y1, secret_key, a, p)
                    print(f"Вычислить открытый ключ: [secret]G = [{secret_key}]({x1}, {y1}) = {open_key}")
                    print("Выберите случайное число больше 0 и меньше порядка =", q)
                    rand = int(input("Введите число: "))
                    if (rand > 0 and rand < q):
                        R = find_composition(x1, y1, rand, a, p)
                        P = find_composition(open_key[0], open_key[1], rand, a, p)
                        print(f"Вычислить R: [rand]G = [{rand}]({x1}, {y1}) = {R}")
                        print(f"Вычислить P(x, y): [rand]open_key = [{rand}]({open_key[0]}, {open_key[1]}) = {P}")
                        message = input("Введите сообщение для шифрования (можно использовать буквы алфавита, цифры, пробел и ! , .): ")
                        for m in message:
                            e = (alphabet.index(m) * P[0]) % p
                            sipher.append(e)
                        print(f"Итог для отправки: (R, e) -> ({R}, {sipher}")
                        print("Расшифрование: ")
                        plain_message = []
                        Q = find_composition(R[0], R[1], secret_key, a, p)
                        print(f"Q = [secret]R = [{secret_key}]{R} ={Q}")
                        for s in sipher:
                            m = (s * pow(Q[0], -1, p)) % p
                            plain_message.append(alphabet[m])
                        print(f"Исходное сообщение: {plain_message}")
                    else:
                        print("Выберите, пожалуйста, число в указанных пределах.")
                else:
                    print("Выберите подходящий секретный ключ.")
            else:
                print("Выберите подходящую точку.")
    elif cmd == "0":
        raise SystemExit
    else:
        print("Вы ввели не правильное значение")




