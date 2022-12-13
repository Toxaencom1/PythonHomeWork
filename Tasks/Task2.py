# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# 0 0 0 0 1 1 1 1
# 0 0 1 1 0 0 1 1
# 0 1 0 1 0 1 0 1.
print("Здравствуй пользователь, эта программа проверяет истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z", end=" ")
print("для всех значений предикат.")
arrayX = [False, False, False, False, True, True, True, True]
arrayY = [False, False, True, True, False, False, True, True]
arrayZ = [False, True, False, True, False, True, False, True]
for i in range(0, 8):
    left = not (arrayX[i] or arrayY[i] or arrayZ[i])
    right = (not arrayX[i]) and (not arrayY[i]) and (not arrayZ[i])
    print(f"x = {arrayX[i]}")
    print(f"y = {arrayY[i]}")
    print(f"z = {arrayZ[i]}")
    print(f"Результат выражения: not(x or y or z) = {left}")
    print(f"Результат выражения: (not x) and (not y) and (not z) = {right}")
    if left == right:
        print("Утверждение Истинно!")
    else:
        print("Утверждение не верно")
    print()
