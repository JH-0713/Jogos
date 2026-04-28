from random import randint
from ferramentas.cor import *
from ferramentas.inputs import *

lista_jogo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_core = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def espaco():
    for i in range(35):
        print('')

def introduzir():
    while True:
        print(f"{negrito()}")
        print(f"""
    ░█████                                            ░██               ░██    ░██            ░██ ░██                   
      ░██                                             ░██               ░██    ░██            ░██ ░██                   
      ░██   ░███████   ░████████  ░███████      ░████████  ░██████      ░██    ░██  ░███████  ░██ ░████████   ░██████   
      ░██  ░██    ░██ ░██    ░██ ░██    ░██    ░██    ░██       ░██     ░██    ░██ ░██    ░██ ░██ ░██    ░██       ░██  
░██   ░██  ░██    ░██ ░██    ░██ ░██    ░██    ░██    ░██  ░███████      ░██  ░██  ░█████████ ░██ ░██    ░██  ░███████  
░██   ░██  ░██    ░██ ░██   ░███ ░██    ░██    ░██   ░███ ░██   ░██       ░██░██   ░██        ░██ ░██    ░██ ░██   ░██  
 ░██████    ░███████   ░█████░██  ░███████      ░█████░██  ░█████░██       ░███     ░███████  ░██ ░██    ░██  ░█████░██ 
                             ░██                                                                                        
                       ░███████                                                                                                                                                                               
            """)
        print("")
        print('')
        print(f'[1] {f_verde()}Jogar{f_reset()}')
        print(f'[2] {f_vermelho()}Sair{f_reset()}')
        print('')
        ex1 = input_int("> ")
        if ex1 == 1:
            espaco()
            return True
        elif ex1 == 2:
            print('')
            print('Até mais!')
            return False
        else:
            print('Error')

def selecionar_xo():
    while True:
        print('')
        print('Escolha com qual jogar:')
        print('')
        print('[1] ❌')
        print('[2] ⭕')
        print('')
        es1 = input_int('> ')
        print('')
        if es1 == 1:
            p1 = "❌"
            c1 = "⭕"
            return p1,c1
        elif es1 == 2:
            p1 = "⭕"
            c1 = "❌"
            return p1,c1
        else:
            print('Selecione ❌ OU ⭕')

def corrigir():
    while True:
        x1, x2, x3, x4, x5, x6, x7, x8, x9 = lista_jogo[0], lista_jogo[1], lista_jogo[2], lista_jogo[3], lista_jogo[4], \
            lista_jogo[5], lista_jogo[6], lista_jogo[7], lista_jogo[8]
        print('')
        print('⚠️ Erro Selecione um NUMERO')
        print('')
        print(f'[{x1}] | [{x2}] | [{x3}]')
        print(f'[{x4}] | [{x5}] | [{x6}]')
        print(f'[{x7}] | [{x8}] | [{x9}]')
        print('')
        e1 = input_int("> ")
        e_1 = e1 - 1
        print('')
        if lista_jogo[e_1] == pl1 or lista_jogo[e_1] == pc1:
            pass
        else:
            return e_1

def corrigir_cpu():
    while True:
        global nr1, nr2
        nr1 = randint(1, 9)
        nr2 = nr1 - 1
        if lista_jogo[nr2] == pl1 or lista_jogo[nr2] == pc1:
            pass
        else:
            return nr2

def decidir():
    x1, x2, x3, x4, x5, x6, x7, x8, x9 = lista_jogo[0], lista_jogo[1], lista_jogo[2], lista_jogo[3], lista_jogo[4], \
        lista_jogo[5], lista_jogo[6], lista_jogo[7], lista_jogo[8]
    if x1 == pl1 and x2 == pl1 and x3 == pl1:
        print('')
        print(f'[{x1}] | [{x2}] | [{x3}]')
        print(f'[{x4}] | [{x5}] | [{x6}]')
        print(f'[{x7}] | [{x8}] | [{x9}]')
        print('')
        return 'Player Wins'
    elif x4 == pl1 and x5 == pl1 and x6 == pl1:
        print('')
        print(f'[{x1}] | [{x2}] | [{x3}]')
        print(f'[{x4}] | [{x5}] | [{x6}]')
        print(f'[{x7}] | [{x8}] | [{x9}]')
        print('')
        return 'Player Wins'
    elif x7 == pl1 and x8 == pl1 and x9 == pl1:
        print('')
        print(f'[{x1}] | [{x2}] | [{x3}]')
        print(f'[{x4}] | [{x5}] | [{x6}]')
        print(f'[{x7}] | [{x8}] | [{x9}]')
        print('')
        return 'Player Wins'
    elif x1 == pl1 and x4 == pl1 and x7 == pl1:
        print('')
        print(f'[{x1}] | [{x2}] | [{x3}]')
        print(f'[{x4}] | [{x5}] | [{x6}]')
        print(f'[{x7}] | [{x8}] | [{x9}]')
        print('')
        return 'Player Wins'
    elif x2 == pl1 and x5 == pl1 and x8 == pl1:
        print('')
        print(f'[{x1}] | [{x2}] | [{x3}]')
        print(f'[{x4}] | [{x5}] | [{x6}]')
        print(f'[{x7}] | [{x8}] | [{x9}]')
        print('')
        return 'Player Wins'
    elif x3 == pl1 and x6 == pl1 and x9 == pl1:
        print('')
        print(f'[{x1}] | [{x2}] | [{x3}]')
        print(f'[{x4}] | [{x5}] | [{x6}]')
        print(f'[{x7}] | [{x8}] | [{x9}]')
        print('')
        return 'Player Wins'
    elif x1 == pl1 and x5 == pl1 and x9 == pl1:
        print('')
        print(f'[{x1}] | [{x2}] | [{x3}]')
        print(f'[{x4}] | [{x5}] | [{x6}]')
        print(f'[{x7}] | [{x8}] | [{x9}]')
        print('')
        return 'Player Wins'
    elif x3 == pl1 and x5 == pl1 and x7 == pl1:
        print('')
        print(f'[{x1}] | [{x2}] | [{x3}]')
        print(f'[{x4}] | [{x5}] | [{x6}]')
        print(f'[{x7}] | [{x8}] | [{x9}]')
        print('')
        return 'Player Wins'

    if x1 == pc1 and x2 == pc1 and x3 == pc1:
        print('')
        print(f'[{x1}] | [{x2}] | [{x3}]')
        print(f'[{x4}] | [{x5}] | [{x6}]')
        print(f'[{x7}] | [{x8}] | [{x9}]')
        print('')
        return 'CPU Wins'
    elif x4 == pc1 and x5 == pc1 and x6 == pc1:
        print('')
        print(f'[{x1}] | [{x2}] | [{x3}]')
        print(f'[{x4}] | [{x5}] | [{x6}]')
        print(f'[{x7}] | [{x8}] | [{x9}]')
        print('')
        return 'CPU Wins'
    elif x7 == pc1 and x8 == pc1 and x9 == pc1:
        print('')
        print(f'[{x1}] | [{x2}] | [{x3}]')
        print(f'[{x4}] | [{x5}] | [{x6}]')
        print(f'[{x7}] | [{x8}] | [{x9}]')
        print('')
        return 'CPU Wins'
    elif x1 == pc1 and x4 == pc1 and x7 == pc1:
        print('')
        print(f'[{x1}] | [{x2}] | [{x3}]')
        print(f'[{x4}] | [{x5}] | [{x6}]')
        print(f'[{x7}] | [{x8}] | [{x9}]')
        print('')
        return 'CPU Wins'
    elif x2 == pc1 and x5 == pc1 and x8 == pc1:
        print('')
        print(f'[{x1}] | [{x2}] | [{x3}]')
        print(f'[{x4}] | [{x5}] | [{x6}]')
        print(f'[{x7}] | [{x8}] | [{x9}]')
        print('')
        return 'CPU Wins'
    elif x3 == pc1 and x6 == pc1 and x9 == pc1:
        print('')
        print(f'[{x1}] | [{x2}] | [{x3}]')
        print(f'[{x4}] | [{x5}] | [{x6}]')
        print(f'[{x7}] | [{x8}] | [{x9}]')
        print('')
        return 'CPU Wins'
    elif x1 == pc1 and x5 == pc1 and x9 == pc1:
        print('')
        print(f'[{x1}] | [{x2}] | [{x3}]')
        print(f'[{x4}] | [{x5}] | [{x6}]')
        print(f'[{x7}] | [{x8}] | [{x9}]')
        print('')
        return 'CPU Wins'
    elif x3 == pc1 and x5 == pc1 and x7 == pc1:
        print('')
        print(f'[{x1}] | [{x2}] | [{x3}]')
        print(f'[{x4}] | [{x5}] | [{x6}]')
        print(f'[{x7}] | [{x8}] | [{x9}]')
        print('')
        return 'CPU Wins'

    for i in range(len(lista_core)):
        if not i in lista_jogo[i]:
            print('flamingo')
        else:
            print('Flame')

w1 = introduzir()
pl1,pc1 = selecionar_xo()
while w1:
    nr1 = randint(1,9)
    nr2 = nr1 - 1
    x1, x2, x3, x4, x5, x6, x7, x8, x9 = lista_jogo[0], lista_jogo[1], lista_jogo[2], lista_jogo[3], lista_jogo[4], \
    lista_jogo[5], lista_jogo[6], lista_jogo[7], lista_jogo[8]

    r1 = decidir()
    if r1 == 'CPU Wins':
        print(r1)
        break

    if r1 == 'Player Wins':
        print(r1)
        break

    print('')
    print('Selecione um Numero:')
    print('')
    print(f'[{x1}] | [{x2}] | [{x3}]')
    print(f'[{x4}] | [{x5}] | [{x6}]')
    print(f'[{x7}] | [{x8}] | [{x9}]')
    print('')
    esc1 = input_int("> ")
    ex1 = esc1 - 1
    print('')
    if esc1 in lista_core:
        if lista_jogo[ex1] == lista_core[ex1]:
            lista_jogo[ex1] = pl1
        else:
            exc1 = corrigir()
            lista_jogo[exc1] = pl1

    r1 = decidir()
    if r1 == 'CPU Wins':
        print(r1)
        break

    if r1 == 'Player Wins':
        print(r1)
        break

    if nr1 in lista_core:
        if lista_jogo[nr2] == lista_core[nr2]:
            lista_jogo[nr2] = pc1
        else:
            exc2 = corrigir_cpu()
            lista_jogo[exc2] = pc1
