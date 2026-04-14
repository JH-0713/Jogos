from random import randint
from ferramentas.inputs import *
from ferramentas.cor import *

ver_cartas = False

lista_jp1 = [0]
lista_p1 = []
lista_jc1 = [0]
lista_c1 = []

p_p1 = 0
p_c1 = 0
p_e1 = 0

def rezetar():
    return [],[0],[],[0]

def espaco():
    for i in range(35):
        print('')

def introduzir():
    while True:
        print(f'{negrito()}')
        print(
            f"""
            ░█████                                        {f_vermelho()} ░██████    ░██  {f_reset()} 
              ░██                                         {f_vermelho()}░██   ░██ ░████  {f_reset()}  
              ░██   ░███████   ░████████  ░███████        {f_vermelho()}      ░██   ░██  {f_reset()}  
              ░██  ░██    ░██ ░██    ░██ ░██    ░██       {f_vermelho()}  ░█████    ░██  {f_reset()}  
        ░██   ░██  ░██    ░██ ░██    ░██ ░██    ░██       {f_vermelho()} ░██        ░██  {f_reset()}  
        ░██   ░██  ░██    ░██ ░██   ░███ ░██    ░██       {f_vermelho()}░██         ░██  {f_reset()}  
         ░██████    ░███████   ░█████░██  ░███████        {f_vermelho()}░████████ ░██████{f_reset()}  
                                     ░██                                    
                               ░███████                                     
                                                                             
            """
        )
        print('')
        print(f'[1] {f_verde()}Jogar{f_reset()}')
        print(f'[2] {f_vermelho()}Sair{f_reset()}')
        print('')
        ex1 = input_int("> ")
        if ex1 == 1:
            espaco()
            return True
        elif ex1 == 2:
            return False
        else:
            print('Error')

def embaralhar():
    for carta in lista_p1:
        if carta == "1":
            carta = "A"
            lista_p1.remove("1")
            lista_p1.append(carta)
        elif carta == "11":
            carta = "J"
            lista_p1.remove("11")
            lista_p1.append(carta)
        elif carta == "12":
            carta = "Q"
            lista_p1.remove("12")
            lista_p1.append(carta)
        elif carta == "13":
            carta = "K"
            lista_p1.remove("13")
            lista_p1.append(carta)

def pedir_carta(e1):
    if e1 == "P":
        p_carta = randint(1, 13)
        p_carta_1 = str(p_carta)
        lista_jp1.append(p_carta)
        lista_p1.append(p_carta_1)

    elif e1 == "C":
        c_carta = randint(1, 13)
        c_carta_1 = str(c_carta)
        lista_jc1.append(c_carta)
        lista_c1.append(c_carta_1)

def parar():
    soma_p = sum(lista_jp1)
    soma_c = sum(lista_jc1)
    print(f"Player: {soma_p}")
    print(f"CPU: {soma_c}")
    if soma_p == 21:
        return "P"
    if soma_c == 21:
        return "C"
    if soma_p == soma_c:
        return "E"
    if soma_p <= 21 and soma_c <= 21:
        if soma_p > soma_c:
            return "P"
        elif soma_p < soma_c:
            return "C"
        elif soma_p == soma_c:
            return "E"
    if soma_p > 21 and soma_c <= 21:
        return "C"
    if soma_p <= 21 and soma_c > 21:
        return "P"
    if soma_p > 21 and soma_c > 21:
        return "E"

def ver_placar():
    print('')
    print('Placar:')
    print('')
    print(f'{f_azul()}Player{f_reset()}: {p_p1}')
    print(f'{f_verde()}CPU{f_reset()}: {p_c1}')
    print('')
    print('Clique em [ENTER] para continuar:')
    input("> ")
    print('')
    espaco()

i1 = introduzir()
while i1:
    embaralhar()
    print(f"")
    print("Escolha:")
    print("")
    print(f"[1] Pedir uma Carta")
    print(f"[2] Parar")
    if ver_cartas == True:
        print(f"[3] Cartas: {f_verde()}{[i for i in lista_p1]}{f_reset()}")
    else:
        print(f'[3] Cartas: {f_vermelho()}[OFF]{f_reset()}')
    print(f"[4] {f_amarelo()}Placar{f_reset()}")
    print(f'[0]{f_vermelho()} Sair {f_reset()}')
    print("")
    carta_esc = input_int("> ")
    print("")
    espaco()

    if carta_esc == 1:
        pedir_carta("P")
        pedir_carta("C")

    elif carta_esc == 2:
        w1 = parar()
        if w1 == "P":
            p_p1 = p_p1 + 1
            print("")
            print(f'Vitoria {f_azul()}Player{f_reset()}')
        elif w1 == "C":
            p_c1 = p_c1 + 1
            print("")
            print(f'Vitoria {f_verde()}CPU{f_reset()}')
        elif w1 == "E":
            p_e1 = p_e1 + 1
            print("")
            print(f'{f_amarelo()}Empate{f_reset()}')

        lista_p1,lista_jp1,lista_c1,lista_jc1 = rezetar()
        print('')
        print('Clique em [ENTER] para continuar:')
        input("> ")
        print('')
        espaco()

    elif carta_esc == 3:
        if ver_cartas == False:
            ver_cartas = True
        else:
            ver_cartas = False

    elif carta_esc == 4:
        ver_placar()

    elif carta_esc == 0:
        break
