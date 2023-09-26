# Solicita a altura e o sexo do usuário
altura = float(input("Digite a altura da pessoa em metros: "))
sexo = input("Digite o sexo da pessoa (M para masculino, F para feminino): ")
# Verifica o sexo e calcula o peso ideal 
if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
    genero = "masculino"
elif sexo.upper() == "F":
    peso_ideal = (62.1 * altura) - 44.7
    genero = "feminino"
else:
    print("Sexo não reconhecido. Use 'M' para masculino ou 'F' para feminino.")
    exit()
# Printa o resultado
print(f"O peso ideal para uma pessoa do sexo {genero} com altura {altura} metros é de {peso_ideal:.2f} quilogramas.")
