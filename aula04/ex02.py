numeros = []
qtdNumeros = int(input("Quantos números você deseja digitar?"))
qtdImpar = 0
media = 0
acum = 0

for num in range(qtdNumeros):
  numeros.append(int(input(f"Digite o número {num + 1}:")))

for idx, numero in enumerate(numeros):
  print((idx + 1), numero)
  
  isEven = numero % 2 != 0
  if isEven:
    qtdImpar += 1
    
  isOdd = numero % 2 == 0
  if isOdd:
    acum += numero
    
media = acum / qtdNumeros

print(f"A quantidade de números ímpares é igual a: {qtdImpar}")
print(f"A media dos números pares é: {media}")


# for idx, numero in numeros:
  