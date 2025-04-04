# funcao de soma 

def soma(a, b, *args):  
    valores = [a, b] + list(args)
    return sum(valores)
'''Essa função declara os argumentos obrigatorios que são a e b, 
o *args tem como função considerar argumentos que não são 
obrigatórios. Em seguida junta todos argumentos em uma única lista
e retorna a soma de todos os valores.
'''

def media(a, b, *args):
    return soma(a, b, *args )/(len(args)+2)
'''Essa função declara os argumentos obrigatorios que são a e b,
o *args tem como função considerar argumentos que não são
obrigatórios. Em seguida utilizei a função soma para os argumentos,
e também a contagem de argumentos com len(args)+2, e dividindo a soma
pela contagem, retornado enfim a média.
'''

a = float(input("Digite um valor:"))
b = float(input("Digite um valor:"))
c = float(input("Digite um valor:"))


print("A soma é:",soma(a, b, c))
print("A média é:", media(a, b, c))


