import random

def gerar_codigo(contagem=0):
    lista_codigo = []
    lista=["1","2","3","4","5","6","7","8","9","0"]
    for i in range(contagem):
        lista_codigo.append(random.choice(lista))
    variavel = "".join(lista_codigo)
    return "PM-"+variavel

print(gerar_codigo(5))