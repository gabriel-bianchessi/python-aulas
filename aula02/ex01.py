# Faça um algoritmo que leia 3 número do usuário.
# Apresente os três números em ordem crescente

print("Insira 3 números diferentes\n")
numero1 = float(input("1:"))
numero2 = float(input("2:"))
numero3 = float(input("3:"))

menor = 0 
meio = 0
maior = 0

if numero1 < numero2 and numero1 < numero3: 
  menor = numero1
  if numero2 < numero3:
    meio = numero2
    maior = numero3
  else: 
    meio = numero3
    maior = numero2

if numero2 < numero3 and numero2 < numero1:
  menor = numero2
  if numero1 < numero3: 
    meio = numero1
    maior = numero3
  else:
    meio = numero3
    maior = numero1

if numero3 < numero2 and numero3 < numero1:
  menor = numero3
  if numero1 < numero2: 
    meio = numero1
    maior = numero2
  else:
    meio = numero2
    maior = numero1



print(f"Ordem decrescente: {menor} < {meio} < {maior}")
