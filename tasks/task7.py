#7 Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
def f7():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                bool_x = bool(x)
                bool_y = bool(y)
                bool_z = bool(z)
                if not (bool_x or bool(y) or bool(z)) == ((not bool_x) and (not bool(y)) and (not bool(z))):
                    print(f"Для значений x = {bool_x}; y = {bool_y}; z = {bool(z)} утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z выполнятется")
                else:
                    print(f"Для значений x = {bool_x}; y = {bool_y}; z = {bool(z)} утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z не выполнятется")
f7()