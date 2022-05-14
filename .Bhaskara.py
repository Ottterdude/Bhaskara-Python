from math import sqrt
a = int(input('Digite o valor de a '))
b = int(input('Digite o valor de b '))
c = int(input('Digite o valor de c '))
delta = int(b ** 2 - 4 * a * c)
x1 = int((-b + (sqrt(delta))) / 2 * a)
x2 = int((-b - (sqrt(delta))) / 2 * a)
print('O valor de x1 é {}, x2 é {} e Delta é {}'.format(x1, x2, delta))
