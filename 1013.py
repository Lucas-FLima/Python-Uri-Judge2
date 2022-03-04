init = input().split()
a = int(init[0])
b = int(init[1])
c = int(init[2])
t = int((a + b + (abs(a - b))) / 2)
if c < t:
    print(f'{t} eh o maior')
else:
    print(f'{c} eh o maior')
