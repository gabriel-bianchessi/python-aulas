a = int(input("Digite a medida do primeiro lado: "))
b = int(input("Digite o segundo lado:"))
c = int(input("Digite o terceiro lado:"))

isTriangule = a + b > c and a + c > b and c + b > a and a > 0 and b > 0 and c > 0

if isTriangule:
  if a == b and b == c: 
    print("É um triângulo Equilátero")
  elif a == b or a == c or b == c:
    print("É um triângulo Isósceles")
  else: 
    print("É um triângulo Escaleno")
else: 
  print("Os valores informados são incapazes de formar um triângulo")