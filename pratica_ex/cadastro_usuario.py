# %%

# Recebe nome, idade, e-mail
# Armazena os dados em uma lista de dicionários
# Mostra todos os cadastros no final

cadastros = []

def sistema():
    while True:
        pessoa = dict()
        pessoa["nome"]  = input("Nome:")
        pessoa["idade"] = input("Idade:")
        pessoa["email"] = input("Email:")
        cadastros.append(pessoa)
    
        continuar = input("Cadastrar outra pessoa?(s/n)").lower()
        if continuar != "s":
            break
        
        
sistema()

for x in cadastros:
    print (x)

# %%
print(cadastros)