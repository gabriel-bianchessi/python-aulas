idade = int(input("Digite a idade do atleta em anos: \nResposta:"))

if idade < 0:
  print("Dados Inválidos")
elif idade > 0 and idade <= 4: 
  print("Infantil")
elif idade >= 5 and idade <= 12:
  print("Criança")
elif idade >= 13 and idade <= 17:
  print("Adolescente")
elif idade >= 18 and idade <= 65:
  print("Adulto")
else: 
  print("Sênior")