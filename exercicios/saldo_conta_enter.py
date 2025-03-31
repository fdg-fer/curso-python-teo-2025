saldo_total = 0

while True:
    deposito = input("Valor depósito:")
    if deposito == "":
        break 
        
    deposito = float(deposito)
    saldo_total = saldo_total + deposito
    

print(saldo_total)
