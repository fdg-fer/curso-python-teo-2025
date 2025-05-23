# Curso Python Teo Me Why 2025

Um curso para iniciantes python, 
aprendendo de forma prática e detalhada
com aulas no youtube.

Esse material tem conteúdos básicos e fundamentos.

-----------------------------------------------------------------

## Tópicos abordados 

-> **Variáveis**\
-> **Condicional**\
-> **Laços de Repetição**\
-> **Estrutura de Dados**\
-> **Funções**
-----------------------------------------------------------------

## Variáveis

```python
x = 10 -> tipo int
x = "café" -> tipo "string"
x = 10.2 -> tipo float
x = True or False -> "booleanos"

input -> forma de o usuário inputar informação
```
------------------------------------------------------------------

## Condicional

if, elif e else

```python
if x == 10:
    print("a")
elif x < 10:
    print("b")
else:
    print("c")
```

------------------------------------------------------------------

## Laços 

**while** -> utilizada quando existe uma concidição declarada.\
Ex: enquanto x for TRUE continuar o laço, quando for FALSE usar BREAK\
para encerrrar o laço.

```python
while True:
    x = int(input("Digite um número: "))  # Solicita um número ao usuário
    if x == 10:  # Correção da comparação
        print(10 * 2)
    else:
        break  # Sai do loop quando x não for 10
```


**for** -> bastante utilizado qunado se quer iterar por uma estrutura de dados.\
Ex: quando se quer iterar sobre uma estrutura de dados, seja uma lista, dicionário ou tupla,\
querendo encontrar uma informação específica.

```python
dic = {"nome":"Fernanda", "idade":34, "cidade":"Goiânia"}

for chave, valor in dic.items():/
    if chave == "Cidade":/
        print(valor)
```
-------------------------------------------------------------------

## Estrutura de dados

```python
Lista = [10, "sal", "café", "relógio", True] -> valores

Dicionario = {"nome":"Fernanda", "idade":34, "cidade":"Goiânia"} -> chave:valor

Tupla = (("nome":"Fernanda"), ("idade":34), ("cidade":"Goiânia")) -> é imutável
Tupla = (("nome":"Fernanda"), ("idade":34), ["cidade":"Goiânia"]) -> apenas a lista é mutável
```

-------------------------------------------------------------------
**Esse foi um dos exercícios propostos que contemplam cada tópico abordado,\
onde todos desempenham sua função em um único programa.**

Escreva um programa que solicite ao usuário frases.
Para parar de solicitar frases, ele pode apenas apertar enter.
Seu programa deve apresentar cada frase e quantas vezes ela foi repetido.

```python
dados = {}

while True:
    frase = input("Digite a frase:")
    if frase == "":
        break
    if frase not in dados:
        dados[frase] = 1
    if frase in dados:
        dados[frase]+=1


for x, y in dados.items():
    print(x, "->" ,y)
```

-------------------------------------------------------------------

## Funções 


**Situação**                           **Use if**      **Use try/except**
Você pode prever o problema                Sim             Não Precisa  
