print("Digite as informações requeridas para obter o salário de um vendedor:")
salarioMinimo = 1212.00
numeroDeCarrosVendidos = int(input("Quantos carros esse funcionário vendeu? "))
valorVendas = float(input("Qual o valor em vendas que o funcionário fez? "))

salario = (salarioMinimo * 2) + (numeroDeCarrosVendidos * 50) + (valorVendas * 0.05)

print(f"O salário total do funcionário é {round(salario, 2)}")