# %%

# Calculadora Simples
## Usuário escolhe a operação (+, -, *, /)
## Digita dois números
## O programa retorna o resultado

operador = input("Qual operação? (+), (-), (*), (/)")

a = int(input("Digite um valor:"))
b = int(input("Digite um valor:"))


def operacao(a,b):
    if operador == "+":
        return a + b
    elif operador == "-":
        return a - b
    elif operador == "*":
        return a * b
    else:
        return a/b
print(a, operador, b)
operacao(a, b)

