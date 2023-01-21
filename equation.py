from tabulate import tabulate

wish = "y"

def print_if_need(line):
    if wish == "y":
        print(line)


def gcd(m, a):
    table_data = []
    a_first = a
    answer = "(" + str(m) + ", " + str(a) + ") = "
    rs = []
    qs = []
    r = 1
    while r != 0:
        q = m // a
        qs.append(q)
        r = m - a*q
        rs.append(r)
        table_data.append([str(m) + " = " + str(a) + "*" + str(q) + " + " + str(r)])
        m, a = a, r
    if rs == [0]:
        qs.insert(0, a_first)
    else:
        qs.insert(0, rs[-2])
    print_if_need(tabulate(table_data))
    print_if_need("НОД" + answer + str(qs[0]))
    return qs

def print_equation (a, b, m):
    print_if_need(str(a) + " x ≡ " + str(b) + " (mod " + str(m) + ")")

def eq (a, b, m):
    table_data = []
    print_equation("a", "b", "m")
    print_equation(a, b, m)
    p = m
    #1
    a %= m
    b %= m
    print_if_need("\n1. Приведём значения в предел модуля:")
    print_equation(a, b, m)
    #2
    print_if_need(f"\n2. Найдём НОД(m, a) -> НОД({m}, {a}):")
    gcd_qs = gcd(m, a)
    d = gcd_qs[0]
    #3
    if (d!=1):
        print_if_need("\n2.1. Проверим кратность b на d(это НОД): b / d = " + str(b//d))
        if (b%d==0):
            a //= d
            b //= d
            m //= d
            gcd(m, a)
            print_equation(a, b, m)
        else:
            return ("Нет решений! b не кратно d")
    n = len(gcd_qs)-1
    # создадим массива для построения строк таблицы
    ns = ["n", " "]
    gcd_qs[0] = "q"
    gcd_qs.insert(1, " ")
    P = ["P", 1]
    for i in range(n):
        ns.append(i+1)
    for t in range(n):
        if t == 0:
            P.append(gcd_qs[t + 2]*P[t + 1])
        else:
            P.append(gcd_qs[t + 2]*P[t + 1] + P[t])
    table_data.append(ns)
    table_data.append(gcd_qs)
    table_data.append(P)
    print_if_need("\n3. Строим таблицу: ")
    print_if_need(tabulate(table_data))
    if (P[-1] == m):
        print_if_need(f"Проверим совпадает ли Pn с m': {P[-1]} = {m}")
    else:
        print("Что-то не так. Ошибка: Pn не совпадает с m'")
    Pn = P[-2]
    print_if_need(f"n = {n}")
    print_if_need(f"Pn-1 = {Pn}")
    #4
    print_if_need("\n4. Нахождение всех решений: xn = x + m'*(n-1) (mod m)")
    xs = []
    print_if_need("\nНахождение x: (-1)^(n-1) * b * Pn-1 (mod m')")
    x = ((-1) ** (n - 1) * b * Pn) % m
    print_if_need(f"x ≡ (-1)^({n-1}) * {b} * {Pn} ≡ {x} (mod {m}) \n")

    for i in range(d):
        xn = (x + m * i) % p
        print_if_need(f"x{i} ≡ {x} + {m}*{i} ≡ {xn} (mod {p})")
        xs.append(xn)
    if len(xs) == 1:
        return xs[0]
    for x in range(len(xs)):
        xs[x] = str(xs[x])
    return xs


#print(eq(6, 18, 23))
#print((72-19)%23)