# Construa um programa que realiza o sorteio de um numero entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa vocÇe deve informar se o chute e maior ou menor que o numero sorteado
# Caso o usário acerte, dê os parabens.

# %%
import random

def get_input():
    while True:
        try:
            numero_usuario = int(input("Digite seu número:"))
        
        except ValueError as arr:
            print("Valor Inválido!")
            continue
        
        if 1 <= numero_usuario <=15:
            return numero_usuario
        
        else:
            print("Valor Inválido. Digite um valor de 1 a 15.")


def check_numbers(usuario, sorteio):

    if usuario == sorteio:
        print("Parabéns! Você é o premiado!")
        return True
    elif usuario < sorteio:
        print("Menor que o número da sorte!")
        return False
    else:   
        print("Maior que o número da sorte!")
        return False
        
numero_sorteio = random.randint(1,15)



for i in range(3):
    
    numero_usuario = get_input()
    if check_numbers(sorteio=numero_sorteio, usuario=numero_usuario):
        break
    
else:
    print("Suas tentativas acabaram")
