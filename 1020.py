i = int(input())
k = [365, 30]
z = 0
for n in k:
    if i >= 365:
        z = int(i / n)
        i = i % 365
    else:
        o = int(i / n)
        t = i % 30
if z != int(0):
    z = z
print(f'{z} ano(s)')
print(f'{o} mes(es)')
print(f'{t} dia(s)')