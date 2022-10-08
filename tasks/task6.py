#6 Дано число обозначающее день недели. 
# Вывести его значение и указать является ли оно выходным днем

def f6():
    days_week = {"1":"Понедельник", "2":"Вторник", "3":"Среда", "4":"Четверг", "5":"Пятница", "6":"Суббота", "7":"Воскресенье"}
    weekend = ["Суббота", "Воскресенье"]
    n = input("Введите число: ")
    day = days_week.get(n)
    if day is None:
        print("Введенное значение не обозначает день недели")
        return
    if day in weekend:
        print(f"{day}: Выходной")
    else:
        print(f"{day}: Не выходной") 
f6()