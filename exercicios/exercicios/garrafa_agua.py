# Faça um programa que vende uma garrafa de agua
# Se o cliente escolher agua mineral natural, será cobrado R$1,50
# Se o cliente escolher agua minaral com gas, sera cobrado R$2,50


pedido = input("Qual água você aceita, com ou sem gás?")
pedido = str(pedido)

if pedido == "com gás":
    print("Custa R$1,50")
    
elif pedido == "sem gás":
    print("Custa R$2,50")
    
else:
    print("Essa opção não existe")

