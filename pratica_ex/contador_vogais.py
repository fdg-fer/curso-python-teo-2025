# Contador de vogais
# Usuário digita uma frase
# Programa mostra quantas vogais tem

# %%

def mostrar_vogais(frase):
    vogais = ["a", "e", "i", "o", "u"] 
    lista = {}
    for letra in frase.lower():
        if letra in vogais:
            if letra in lista:
                lista[letra] += 1
            else:
                lista[letra] = 1

        
    return lista 

  
frase = input("Digite a frase:")

resultado = mostrar_vogais(frase)

for x in resultado:
    print(x, "->", resultado[x])







