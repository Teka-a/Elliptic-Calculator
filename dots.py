from tabulate import tabulate

wish = "n"

def print_if_need(line):
    if wish == "y":
        print(line)

def find_quadratic_residues(p):
    residues = []
    nums = {}
    table_residues = []
    for i in range(p):
        line = []
        y2 = (i ** 2)
        residue = y2 % p
        if residue in nums:
            mas = nums.get(residue)
            mas.append(i)
            nums[residue] = nums.get(residue)
        else:
            nums[residue] = [i]
        line.extend((i, y2, residue))
        residues.append(residue)
        table_residues.append(line)
    sorted_residues = dict(sorted(nums.items(), key=lambda x: x[0]))
    #print(sorted_residues)
    print_if_need("Таблица квадратов по модулю " + str(p) + ":")
    print_if_need(tabulate(table_residues, headers=["y", "y^2", "y^2%p"]))
    return sorted_residues

def find_dots(a, b, p):
    table_dots = []
    # массив точек содержит точки в виде массива [x,y] : dots = [[x,y],[x,y]]
    dots = []
    # словарь для соответсвия y^2 : квадратичный вычет
    quadratic_residues = {}

    quadratic_residues = find_quadratic_residues(p)

    for x in range(p):
        dots_y = []
        dots_round = []
        ys = []
        line = []
        y2 = (x ** 3 + a*x + b) % p
        equation = "y^2 = " + str(x) + "^3 + " + str(a*x) + " + " + str(b)
        if (y2 in quadratic_residues):
            mas = quadratic_residues.get(y2)
            for o in mas:
                ys.append(str(o))
                dot = [x, o]
                dots_y.append(dot)
                dots.append(dot)
        if ys == [] and dots_y == []:
            ys.append("y не существует")
            dots_y.append("y не существует")
        ys_str = ", ".join(ys)
        for d in dots_y:
            if d != "y не существует":
                dot = "(" + str(d[0]) + ", " + str(d[1]) + ")"
                dots_round.append(dot)
            else:
                dots_round.append(d)
        dots_y_str = ", ".join(dots_round)
        line.extend((x, equation, y2, ys_str, dots_y_str))
        table_dots.append(line)
    print_if_need(tabulate(table_dots, headers=["x", "Уравнение", "y^2%p", "Соответсвующие y", "Точки"]))
    count_dots = len(dots)+1
    print("Всего точек (включая О): " + str(count_dots))
    return dots

#print(find_dots(3, 4, 11))
