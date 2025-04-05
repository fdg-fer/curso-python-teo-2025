# %%

def calc_imposto(preco, tx_base, **kwargs):
    imposto = preco * tx_base
    
    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]
    """Essa funcao faz o calculo de impostos, os parametros
definidos sao preco e taxa base, o argumento **kwargs representa um conjunto de
elementos do tipo dicionário que também contemplam o calculo, quando existem.
A estrutura de laço de repetição é justamente para iterar sobre o dicionário(kwargs)
é incluir os valores(impostos gerais) no imposto total.s
    """        
    return imposto

# %%

impostos_gerais = {"federal" : 0.02,
                   "estadual": 0.05,
                   "municipal": 0.08}

calc_imposto(100, 0.03, **impostos_gerais)

