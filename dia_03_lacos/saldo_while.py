saldo = 0


while True:
    valor = input("Digite um valor: ")
    if valor == "":
        break
    
    saldo += float(valor) 
    
print("Saldo total:", saldo)