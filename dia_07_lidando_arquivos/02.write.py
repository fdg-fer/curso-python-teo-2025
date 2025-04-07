# %%

# ## Aqui diferente do read que faz a leitura do arquivo, o write insere 
# ## informações no arquivo, que no caso aqui o mode pode sera para 
# ## sobrescrever "w" ou aicionar "a"

txt = "O nome do arquivo."

nome_arquivo = "texto_2.txt"

with open(nome_arquivo, mode="w") as open_file:
    open_file.write(txt)
    
# %%

with open(nome_arquivo, mode="a") as open_file:
    open_file.write(txt)