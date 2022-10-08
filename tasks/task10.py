#10 Найти расстояние между двумя точками пространства
def f10():
    import math
    try:
        x_A = float(input("Введите координату X точки A: "))
        y_A = float(input("Введите координату Y точки A: "))
        x_B = float(input("Введите координату X точки B: "))
        y_B = float(input("Введите координату Y точки B: "))
    except ValueError:
        print("Введено не число")
        return

    result = math.sqrt(math.pow(x_A - x_B, 2) + math.pow(y_A - y_B, 2))
    print('{:.2f}'.format(result))  
f10()