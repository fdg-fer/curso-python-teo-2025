# Faça uma programa que conte quantas vezes a letra "a" aparece em uma palavra
palavra = input("Digite uma palavra:")
total = 0

for x in palavra:
   if x == 'a':
       total = total + 1
    
print(total)     
    
    