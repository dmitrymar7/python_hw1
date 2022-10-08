#8 Сообщить в какой четверти координатной плоскости находится точка с координатами X и Y
def f8():
    try:
        x = float(input("Введите число x: "))
        y = float(input("Введите число y: "))
    except ValueError:
        print("Введено не число")
        return   
    if x > 0 and y > 0:
        print("1 четверть")
    elif x < 0 and y > 0:
        print("2 четверть")
    elif x < 0 and y < 0:
        print("3 четверть")
    elif x > 0 and y < 0:
        print("4 четверть")
    else:
        print("Точка находится на оси")
f8()