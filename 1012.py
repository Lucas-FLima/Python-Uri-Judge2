init = input().split()
a = float(init[0])
b = float(init[1])
c = float(init[2])
pi = 3.14159
trir = (a * c) / 2
cir = (pi * (c ** 2))
tra = ( (a + b) * c) / 2
qua = (b ** 2)
ret = (a * b)
print(f'TRIANGULO: {trir:.3f}')
print(f'CIRCULO: {cir:.3f}')
print(f'TRAPEZIO: {tra:.3f}')
print(f'QUADRADO: {qua:.3f}')
print(f'RETANGULO: {ret:.3f}')
