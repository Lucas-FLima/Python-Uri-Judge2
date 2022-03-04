val = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
print(val)
for n in notas:
    qtd_nota = int((val / n))
    print(f'{qtd_nota} nota(s) de R$ {n},00')
    resto = val % n
    val = resto

