print("Dogote um número e deixe que a outra pessoa adivinhe o número que você pensou")
numero = int(input("Qual número você está pensando? "))
for num in range(10):
  print("\n")

numeroTentativas = 0

while True:
  numeroTentativas += 1
  chute = int(input("Qual seu chute? "))
  if chute == numero:
    print(f"Parabéns! Você acertou em {numeroTentativas} tentativas")
    break 
  if chute > numero:
    print("Seu chute foi alto, tente de novo")
  if chute < numero:
    print("Seu chute foi baixo, tente novamente")

  