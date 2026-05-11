soma = 0
print("Digite uma sequência de valores (0 encerra: ): ")

while True:
    n = int(input())
    if n == 0:
        break
    soma += n
print(f'O resultado da soma é: {soma}')
