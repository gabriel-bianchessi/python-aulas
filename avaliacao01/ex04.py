# notas multiplicadas pelos pesos e depois divididas pela soma dos pesos
print("Informe as notas e pesos para obter o conceito do aluno:")

nome = input("Qual o nome do aluno: ")

atividade1 = input("Qual foi a atividade desenvolvida para a Nota 1 ")
nota1 = int(input("Digite a nota 1 "))
peso1 = int(input("Digite o peso para a nota 1 "))
atividade2 = input("Qual foi a atividade desenvolvida para a Nota 2 ")
nota2 = int(input("Digite a nota 2 "))
peso2 = int(input("Digite o peso para a nota 2 "))
atividade3 = input("Qual foi a atividade desenvolvida para a Nota 3 ")
nota3 = int(input("Digite a nota 3 "))
peso3 = 10 - (peso1 + peso2)

mediaPonderada = ((nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)) / (peso1 + peso2 + peso3)

if mediaPonderada >= 8:
  conceito = "A"
elif mediaPonderada >= 7 and mediaPonderada < 8:
  conceito = "B"
elif mediaPonderada >= 6 and mediaPonderada < 7:
  conceito = "C"
elif mediaPonderada >= 5 and mediaPonderada < 6:
  conceito = "D"
elif mediaPonderada >= 0 and mediaPonderada < 5:
  conceito = "E"
  
print(f"O aluno {nome} recebeu o conceito {conceito}, com a media {mediaPonderada}.")
print("Ele resolveu as seguintes atividades:")
print(f"Atividade 1: {atividade1}, Nota: {nota1}, Peso: {peso1}")
print(f"Atividade 2: {atividade2}, Nota: {nota2}, Peso: {peso2}")
print(f"Atividade 3: {atividade3}, Nota: {nota3}, Peso: {peso3}")