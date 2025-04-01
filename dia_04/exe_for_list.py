# %%
# Escreva um programa que receba uma lista de números
# do usuario e conte quantas vezes um número
# específico aparece na lista
# solicite ao usuário um numero e exiba a contagem

lista = [5,4,4,8,8,7,8,9,6,1,7,2,3,6,0,0,1,5,4]
numero = int(input("Digite um numero:"))
contador = 0

for x in lista:
    if x == numero:
        contador+=1
print(contador)

# %%

lista = []

while True:
    numero = input("Digite um valor:")
    if numero == "":
        break
    else:
        lista.append(int(numero))
        
print(lista)
