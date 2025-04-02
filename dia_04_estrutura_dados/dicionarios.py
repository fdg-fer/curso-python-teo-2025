# %%
info = {"nome": "camila", "status": "namorando", "profissao": "advogada", "altura": "1,75", "filhos": False }

type(info)

# %%

info["nome"]

print(info.keys())
print(info.values())
print(info.items())

# %%
dic = {"nome":"fernanda",
       "profissao":["enegenheira_de_dados", "analista_de_dados", "analista_operaional"],
       "formacao":"tecnologia_geoprocessamento", 
       "cursos_complementares":[{"cursos_complementar":"Git e Github", "professor":"Teo Me Why",
                                 "cursos_complementar":"Introdução_Python","professor":"Teo Me Why"}]}


dic["profissao"][2]

# %%

for x in dic:
    print(x, "-->", dic[x])

# %%

for x, y in dic.items():
    print(x, "-->",y)
    
# %%

tupla = (34, "Fernanda", ["azul","preto", "amarelo"], "goiania")

print(type(tupla))

tupla[2].append("verde")

print(tupla)