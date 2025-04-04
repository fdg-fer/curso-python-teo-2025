
def par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"
        
numero = input("Digite um valor:")
numero = int(numero)

resultado = par_impar(numero)

print("O número", numero, "é ->", resultado)
