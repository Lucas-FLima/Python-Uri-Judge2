dado = int(input())
base = 60
h = base ** 2
hour = int(dado / h)
min = int((dado % h) / base)
seg = ((dado % h) - (min * base))
print(f'{hour}:{min}:{seg}')