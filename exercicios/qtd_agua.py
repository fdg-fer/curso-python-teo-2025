texto = """
Escolha a sua água para comprar
(1) Água mineral natural
(2) Água mineral com gás
 """
 
opcao = input(texto)

valor_item = 0
if opcao == "1":
    valor_item = 1.5 

elif opcao =="2":
    valor_item = 2.5
 
    
if valor_item == 0:
    print("Entre com a opção correta")

else:
    qtd = input("Qunatas garrafas você quer?")
    qtd = int(qtd)
    valor_total = qtd * valor_item

    print("A sua compra custa R$", valor_total)   