# informar o peso e idade do jogador 

nome = input("Qual o nome do competidor? ")
peso = float(input("Qual o peso do competidor? "))
idade = int(input("Qual a idade do competidor? "))

if (idade >= 0 and idade < 18) and peso <= 50:
  print(f"{nome} - Insuficiente para participar")

if (idade < 18 and idade >= 0) and peso > 50:
  print(f"{nome} - Júnior")
  
if idade > 18 and peso < 50: 
  print(f"{nome} - Mini")
  
if idade > 18 and peso > 50:
  print(f"{nome} - Pleno")