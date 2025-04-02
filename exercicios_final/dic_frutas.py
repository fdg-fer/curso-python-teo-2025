# Soilicite ao usuario o nome de uma fruta 
# e exiba o preço correspondente

# %%
mercado = {"Maçã": "R$8,00 kg", "Banana":"R$4,99 kg", "Uva":"R$9,00 kg",
           "Coco":"R$7,00 kg", "Morango":"R$12,00 kg", "Abacaxi":"R$15,00 kg" }

compra = input("Consulta Preço:")

for x, y in mercado.items():
    if compra == x:
        print("Fruta:",x,"--> Valor:",y)



