# Pede o peso dos peixes ao usuário
peixes = float(input("Digite o peso de peixes em quilogramas: "))

limite = 50.0
if peixes > limite:
    excesso = peixes - limite
    multa = excesso * 4.0
else:
    excesso = 0
    multa = 0

# Printa o resultado
if excesso > 0:
    print(f"Peso excedente de {excesso:.3f} quilogramas.")
    print(f"Valor da multa a pagar: R$ {multa:.1f}")
else:
    print("Peso dentro do limite permitido em São Paulo. Sem valor a pagar.")
# Seria o João, um mentiroso? papo de pescador isso ai
