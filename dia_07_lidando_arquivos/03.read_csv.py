# %%

# Declaracao do arquivo csv

arquivo = "data.csv"

# Abertura leitura do arquivo retornando um lista de elementos por linha com o uso de "readlines"
with open(arquivo) as open_file:
    lines = open_file.readlines()

lines   

# %%
 
for l in lines:
    print(l)
    
# %%
#Criando um dicionario para receber os dados
dados = dict()
     
  
# Declarando quais serão as chaves, para isso foi utilizado strip para o "\n" e split que 
# divide a string em partes com base no separador ";" retornando os dados em lista. 
# Observacao é que as chaves estão no índice "[0]"

chaves = lines[0].strip("\n").split(";")
for c in chaves:
    dados[c] = []
    
dados


# Declarando os valores, podemos assumir que os valores estão a partir da linha [1], em cada linha 
# divide a string em partes com base no separador ";" retornando os dados em lista.

# Com as chaves e valores definidos vamos iterar com um range com base na quantidade de valores. 
# cada iteracao amarra na segunda linha de comando os "chave:valor", fazendo um append de cada
# valor em sua respectiva valor.
    
for l in lines[1:]:
    valores = l.strip("\n").split(";")

    for i in range(len(valores)):
        dados[chaves[i]].append(valores[i])
        
dados
    
# %%

# Aqui a iteracao é para converter os valores de idade para int e depois 
# calcular a média.

idade=[]

for i in dados["idade"]:
    idade.append(int(i))
    
media = sum(idade)/len(idade)
media
    