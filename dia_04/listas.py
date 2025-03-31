# %% 

# Uma maneira ed definir listas 
idades = [28,32,14,1,14,78]
print(idades)

# %%

lista = ["Teo", "Fernanda", 14, True, "Python", 1254.14]
print(lista)

# %%
type(lista)

# %%

print(lista[2])

# %%

idades = [28,5,65,24,12,82,2,34]

soma = sum(idades)
print("Soma:",soma)

print(len(idades))

print(soma/len(idades))

print(max(idades))

print(min(idades))

# %%

lista = ["Teo", "Fernanda", 14, True, "Python", 1254.14,["Chave", "Bike", "Mouse"]]

print(lista[6][0])

# %%

# leitura tamnho de elementos da lsita
tamanho = len(lista)

# identificando o o último elemento da lista
pos = tamanho - 1

# gerando variavel o último da elemnto de lista
obj = lista[pos]

# identificando o último elemto da lista que está dentro de outra lista
lista[pos][len(obj)-1]

# identificando o último elemto da lista que está dentro de outra lista 
lista[-1][-1]

# %%

# particionando parte da lista
lista[0:4]

# particionando lista dentro de outra lista     
lista[6][1:3]

# poderíamos definir como [start:stop]
# não definir o start ou stop considera os elementos desde o início ou até fim da lista
lista[:3]

# aqui é [start : stop : step]
# nesse caso o step é passo que eu vou dar, ou seja vou pular x elementos
lista[::2]