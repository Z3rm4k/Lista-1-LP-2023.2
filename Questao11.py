# definição dos valores
num_int = int(input("Digite o primeiro número inteiro: "))
num_int1 = int(input("Digite o segundo número inteiro: "))
num_r = float(input("Digite um número real: "))

# faz as operações
r1 = (2 * num_int) * (num_int1 / 2)
r2 = (3 * num_int) + num_r
r3 = num_r ** 3

# printa os resultados
print(f"O produto do dobro do primeiro número com metade do segundo número é: {r1}")
print(f"A soma do triplo do primeiro número com o número real é: {r2}")
print(f"O número real elevado ao cubo é: {r3}")
