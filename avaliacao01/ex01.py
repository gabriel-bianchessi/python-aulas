numero = int(input("Digite o número do funcionário: "))
nome = input("Digite o nome do funcionário: ")
horasTrabalhadas = int(input("Digite o número de horas trabalhadas: "))
valorPorHora = float(input("Digite o valor por hora do funcionário: "))

salario = valorPorHora * horasTrabalhadas

print(f"O funcionário nº{numero}, {nome}, ganhará R${round(salario, 2)}")