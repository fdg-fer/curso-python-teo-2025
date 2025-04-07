
# %%
palavra = input("Digite uma palavra:")


if palavra.lower() == palavra[::-1].lower():
    print("Palíndromo")
else:
    print("Não é palíndromo")
    
    
print(palavra)