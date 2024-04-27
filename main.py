def add(x,y):
  return x + y

def sub(x,y):
  return x - y
  
def mult(x,y):
  return x * y

def div(x,y):
  return x / y
  
#print (" oi ") mostra informação em ("") na tela
#variavel armazena informação
#Ipunt armazena o que o usuario digita
#float numero com virgula
#integer - numero inteiro
#string - textos
#boolean - true or false

print ("Selecione uma operação.")
print ("1. Adição")
print ("2. Subtração")
print ("3. Multiplicação")
print ("4. Divisão")

escolha = input("Escolha uma operação (1/2/3/4)")

if escolha in ('1','2','3','4'):
  num1 = float(input("Digite um número: "))
  num2 = float(input("Digite outro número: "))

  if escolha == '1':
    print(num1, "+", num2, "=" , add(num1,num2))
    print(add(num1,num2))

  if escolha == '2':
    print(sub(num1,num2))

  if escolha == '3':
    print(mult(num1,num2))

  if escolha == '4':
    print(div(num1,num2))
    
  else:
    print("Opção inválida")
 
