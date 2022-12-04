print('Решаем уравнение a•x²+b•x+c=0')
a = input('Введите значение a: ')
b = input('Введите значение b: ')
c = input('Введите значение c: ')

a = float(a)
b = float(b)
c = float(c)

discriminant = (b ** 2) - (4 * a * c)

if discriminant < 0:
    print("No square roots")
elif discriminant == 0:
    x = -b / (2 * a)
    print(f"This equation has one square root which equals to {x}")
else:
    x1 = (-b + discriminant ** 0.5 ) / (2 * a)
    x2 = (-b - discriminant ** 0.5 ) / (2 * a)
    print(f"This equation has two square roots: x1: {x1} and x2: {x2}")