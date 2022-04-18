a = int(input("Digite um número para a variável A: "))
b = int(input("Digite um número para a variável B: "))

while True:
  if a >= 100 and b <= 200:
    break
  
  if a < 100:
    print("A variável A foi digitada errado :(")
    a = int(input("Digite A novamente: "))
  
  if b > 200:
    print("A variável B foi digitada errado :(")
    b = int(input("Digite B novamente: "))
    
print(f"Os valores foram digitados corretamente. A: {a}, B: {b}")