# %%
nome_arquivo = "texto.txt"

# # Abre, faz leitura e e fecha arquivo
# # Esse trecho é uma mlehor prática
with open(nome_arquivo) as open_file:
    conteudo = open_file.read()
    
print(conteudo)


# # Abre o arquivo em formato de leitura 
#open_file = open(nome_arquivo)


# # Lê os dados do arquivo 
#conteudo = open_file.read()
#print(conteudo)

# # Fecha o arquivo
#open_file.close()


