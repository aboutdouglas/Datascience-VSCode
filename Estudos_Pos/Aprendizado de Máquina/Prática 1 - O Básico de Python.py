# Exercicio 1
a = int(input("Digite o valor de seu Salário Bruto: R$"))
IR = a * 11 / 100
INSS = a * 8 / 100
Sindicato = a * 5 / 100
Descontos = IR + INSS + Sindicato
Liquido = a - Descontos
print("Seu Salário Líquido é: R$", Liquido)

# Exercício 2
ga = int(input("Informe a nota do Grau A: "))
gb = int(input("Informe a nota do Grau B: "))
media = (ga + gb) / 2
print("A Média do aluno é: ", media)

if media >= 9:
     print('Nota A')
elif media >= 7.5 and media < 9:
     print('Nota B')
elif media >= 6 and media < 7.5:
     print('Nota C')
elif media >= 4 and media <= 6:
     print('Nota D')
else:
     print('Nota E')
     
     
# Exercício 3
x = int(input("Informe o valor que você deseja saber a tabuada: "))
for i in range(1, 11):
     print(x*i)
     
     
# Exercício 4
usuario = input("Informe o usuário: ")
senha = input("Informe a senha: ")
while usuario == senha:
    print("Nome do Usuário não pode ser igual a Senha")
    break
else:
   print("Usuário Criado")
   

# Exercício 5
uma_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nova_lista = list(reversed(uma_lista))
print(nova_lista)

# Exercício 6
cliente = ["Fernanda", "Montenegro", 1929, "Central do Brasil", 1998, "Atriz", "Rio de Janeiro, RJ"]
cliente.append(input("Informe a próxima Informação: "))
while "fim" not in cliente:
    print(cliente)
    cliente.append(input("Informe a próxima Informação: "))
else:
    print("fim")
    

# Exercício 8
palavra1 = input('String 1: ')
palavra2 = input('String 2: ')

print('Tamanho de "%s": %d ' % (palavra1, len(palavra1)))
print('Tamanho de "%s": %d ' % (palavra2, len(palavra2)))
if len(palavra1) == len(palavra2):
    print("Strings são de tamanhos iguais")
else:
  print("Strings são de tamanhos diferentes")
if palavra1 == palavra2:
  print("Strings são iguais")
else:
  print("Strings são diferentes")
  

# Exercício 9
nome = input("Digite o seu nome: ")
nomeMaiusculo = nome.upper()
nomeInvertido = nomeMaiusculo[::-1]
print(nomeMaiusculo)
print(nomeInvertido)
