# Escreva um programa que solicite ao usuário frases.
# Para parar de solicitar frases, ele pode apenas apertar 

# Seu programa deve apresentar cada frase e quantas vezes ela foi repetido.

dados = {}

while True:
    frase = input("Digite uma frase:")
    if frase == "":
        break 

    if frase not in dados:
        dados[frase] =1
    else:
        dados[frase]+=1
        
 
for x in dados:
    print(x,"-->",dados[x])
