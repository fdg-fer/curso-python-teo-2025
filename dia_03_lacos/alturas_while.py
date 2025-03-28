soma  = 0 
qtd_entradas = 4 

while qtd_entradas > 0:
    altura = input("Altura: ")
    altura = float(altura)
    soma += altura
    qtd_entradas -=1

print("Soma das alturas:", soma)