# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#
# Пример:
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print("Здравствуй пользователь, эта программа находит расстояние между двумя точками в 2D пространстве. ")
print("Введите координаты точки A")
aX = int(input("Введите X: "))
aY = int(input("Введите Y: "))
print("Введите координаты точки B")
bX = int(input("Введите X: "))
bY = int(input("Введите Y: "))

print(f"A({aX},{aY}) B({bX},{bY})")

AB = ((bX-aX)**2+(bY-aY)**2)**0.5
print(f'Расстояние между точками A и B = "{round(AB,3)}"')
