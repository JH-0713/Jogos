from random import randint
from ferramentas.inputs import *
from ferramentas.cor import *

sequencia = 0

lj1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lc1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def iniciar():
    while True:
        print(f'''{negrito()}
        {f_verde()}    ░█████                                 {f_reset()}           ░██               {f_rosa()}░██    ░██            ░██ ░██                   {f_reset()}
        {f_verde()}      ░██                                  {f_reset()}           ░██               {f_rosa()}░██    ░██            ░██ ░██                   {f_reset()}
        {f_verde()}      ░██   ░███████   ░████████  ░███████ {f_reset()}     ░████████  ░██████      {f_rosa()}░██    ░██  ░███████  ░██ ░████████   ░██████   {f_reset()}
        {f_verde()}      ░██  ░██    ░██ ░██    ░██ ░██    ░██{f_reset()}    ░██    ░██       ░██     {f_rosa()}░██    ░██ ░██    ░██ ░██ ░██    ░██       ░██  {f_reset()}
        {f_verde()}░██   ░██  ░██    ░██ ░██    ░██ ░██    ░██{f_reset()}    ░██    ░██  ░███████     {f_rosa()} ░██  ░██  ░█████████ ░██ ░██    ░██  ░███████  {f_reset()}
        {f_verde()}░██   ░██  ░██    ░██ ░██   ░███ ░██    ░██{f_reset()}    ░██   ░███ ░██   ░██     {f_rosa()}  ░██░██   ░██        ░██ ░██    ░██ ░██   ░██  {f_reset()}
        {f_verde()} ░██████    ░███████   ░█████░██  ░███████ {f_reset()}     ░█████░██  ░█████░██    {f_rosa()}   ░███     ░███████  ░██ ░██    ░██  ░█████░██ {f_reset()}
        {f_verde()}                             ░██           {f_reset()}                                                                             
        {f_verde()}                       ░███████            {f_reset()}                                                                             
        ''')
        print('')
        print(f'[1] {f_verde()}Jogar{f_reset()}')
        print(f'[2] {f_vermelho()}Sair{f_reset()}')
        print('')
        ex1 = input_int("> ")
        if ex1 == 1:
            return True
        elif ex1 == 2:
            return False
        else:
            pass

def selecionar():
    while True:
        print('')
        print('Selecione 1 ou 2:')
        print(f'[1] {f_vermelho()}⨉{f_reset()}')
        print(f'[2] {f_azul()}◯{f_reset()}')
        print('')
        ex1 = input_int("> ")
        print('')
        if ex1 == 1:
            return f'{f_vermelho()}⨉{f_reset()}',f'{f_azul()}◯{f_reset()}'
        elif ex1 == 2:
            return f'{f_azul()}◯{f_reset()}',f'{f_vermelho()}⨉{f_reset()}'
        else:
            pass

def corrigir():
    while True:
        espacar()
        print(f'{negrito()}')
        print('')
        print(f'[{x1}]|[{x2}]|[{x3}]')
        print(f'[{x4}]|[{x5}]|[{x6}]')
        print(f'[{x7}]|[{x8}]|[{x9}]')
        print('')
        print('Selecione um numero sem ⭕/❌:')
        pl2 = input_int("> ")
        print('')
        if pl2 in lj1 and pl2 in lc1:
            return pl2
        elif not pl2 in lj1 and pl2 in lc1:
            pass
        else:
            pass

def corrigir_cpu():
    while True:
        numr2 = randint(1,9)
        if numr2 in lj1 and numr2 in lc1:
            return numr2
        elif not numr2 in lj1 and numr2 in lc1:
            pass
        else:
            pass

def ver_vitoria():

    ## PLAYER
    if lj1[0] == s_p1 and lj1[1] == s_p1 and lj1[2] == s_p1:
        return f'{f_ciano()}Player {f_amarelo()}Wins{f_reset()}'
    elif lj1[3] == s_p1 and lj1[4] == s_p1 and lj1[5] == s_p1:
        return f'{f_ciano()}Player {f_amarelo()}Wins{f_reset()}'
    elif lj1[6] == s_p1 and lj1[7] == s_p1 and lj1[8] == s_p1:
        return f'{f_ciano()}Player {f_amarelo()}Wins{f_reset()}'

    elif lj1[0] == s_p1 and lj1[3] == s_p1 and lj1[6] == s_p1:
        return f'{f_ciano()}Player {f_amarelo()}Wins{f_reset()}'
    elif lj1[1] == s_p1 and lj1[4] == s_p1 and lj1[7] == s_p1:
        return f'{f_ciano()}Player {f_amarelo()}Wins{f_reset()}'
    elif lj1[2] == s_p1 and lj1[5] == s_p1 and lj1[8] == s_p1:
        return f'{f_ciano()}Player {f_amarelo()}Wins{f_reset()}'

    elif lj1[0] == s_p1 and lj1[4] == s_p1 and lj1[8] == s_p1:
        return f'{f_ciano()}Player {f_amarelo()}Wins{f_reset()}'
    elif lj1[2] == s_p1 and lj1[4] == s_p1 and lj1[6] == s_p1:
        return f'{f_ciano()}Player {f_amarelo()}Wins{f_reset()}'

    ## CPU
    if lj1[0] == s_c1 and lj1[1] == s_c1 and lj1[2] == s_c1:
        return f'{f_vermelho()}CPU {f_amarelo()}Wins{f_reset()}'
    elif lj1[3] == s_c1 and lj1[4] == s_c1 and lj1[5] == s_c1:
        return f'{f_vermelho()}CPU {f_amarelo()}Wins{f_reset()}'
    elif lj1[6] == s_c1 and lj1[7] == s_c1 and lj1[8] == s_c1:
        return f'{f_vermelho()}CPU {f_amarelo()}Wins{f_reset()}'

    elif lj1[0] == s_c1 and lj1[3] == s_c1 and lj1[6] == s_c1:
        return f'{f_vermelho()}CPU {f_amarelo()}Wins{f_reset()}'
    elif lj1[1] == s_c1 and lj1[4] == s_c1 and lj1[7] == s_c1:
        return f'{f_vermelho()}CPU {f_amarelo()}Wins{f_reset()}'
    elif lj1[2] == s_c1 and lj1[5] == s_c1 and lj1[8] == s_c1:
        return f'{f_vermelho()}CPU {f_amarelo()}Wins{f_reset()}'

    elif lj1[0] == s_c1 and lj1[4] == s_c1 and lj1[8] == s_c1:
        return f'{f_vermelho()}CPU {f_amarelo()}Wins{f_reset()}'
    elif lj1[2] == s_c1 and lj1[4] == s_c1 and lj1[6] == s_c1:
        return f'{f_vermelho()}CPU {f_amarelo()}Wins{f_reset()}'

def verificar():
    global lj1,lc1, sequencia
    sequencia = 0
    for i in lj1:
        if i == s_p1 or i == s_c1:
            sequencia += 1
            if sequencia == len(lj1):
                return False
        else:
            return True

def espacar():
    for i in range(30):
        print('')

def perguntar():
    while True:
        print(f"{negrito()}")
        print(f"Deseja continuar? [{f_verde()}S{f_reset()}/{f_vermelho()}N{f_reset()}]")
        print("")
        ex1 = input_str("> ").upper()
        print("")
        if ex1 == "S" or ex1 == "SI" or ex1 == "SIM":
            print("Ok recomeçando jogo...")
            print('')
            return True
        elif ex1 == "N" or ex1 == "NA" or ex1 == "NÃ" or ex1 == "NAO" or  ex1 == "NÃO":
            print('Saindo do Jogo...')
            return False
        else:
            pass

def finalizar():
    espacar()
    print(f'{negrito()}Deu Velha')
    print('')
    print(f'[{x1}]|[{x2}]|[{x3}]')
    print(f'[{x4}]|[{x5}]|[{x6}]')
    print(f'[{x7}]|[{x8}]|[{x9}]')
    print('')
    print('Aperte a tecla [ENTER] para continuar:')
    input('> ')

w1 = iniciar()
espacar()
if w1 == True:
    s_p1,s_c1 = selecionar()

x1,x2,x3,x4,x5,x6,x7,x8,x9 = lj1[0],lj1[1],lj1[2],lj1[3],lj1[4],lj1[5],lj1[6],lj1[7],lj1[8]
v_sim = False
while w1:
    if v_sim == True:
        v_sim = False

    numr1 = randint(1,9)
    x1, x2, x3, x4, x5, x6, x7, x8, x9 = lj1[0], lj1[1], lj1[2], lj1[3], lj1[4], lj1[5], lj1[6], lj1[7], lj1[8]

    v1 = ver_vitoria()
    v2 = verificar()
    espacar()

    if v2 == False:
        finalizar()
        espacar()
        c1 = perguntar()
        if c1 == False:
            break
        else:
            lj1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            v_sim = True

    elif v1 == f'{f_ciano()}Player {f_amarelo()}Wins{f_reset()}':
        espacar()
        print('')
        print(v1)
        print('')
        print(f'[{x1}]|[{x2}]|[{x3}]')
        print(f'[{x4}]|[{x5}]|[{x6}]')
        print(f'[{x7}]|[{x8}]|[{x9}]')
        print('')
        print('Aperte a tecla [ENTER] para continuar:')
        input('> ')
        espacar()
        c1 = perguntar()
        if c1 == False:
            break
        else:
            lj1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            v_sim = True

    elif v1 == f'{f_vermelho()}CPU {f_amarelo()}Wins{f_reset()}':
        espacar()
        print('')
        print(v1)
        print('')
        print(f'[{x1}]|[{x2}]|[{x3}]')
        print(f'[{x4}]|[{x5}]|[{x6}]')
        print(f'[{x7}]|[{x8}]|[{x9}]')
        print('')
        print('Aperte a tecla [ENTER] para continuar:')
        input('> ')
        espacar()
        c1 = perguntar()
        if c1 == False:
            break
        else:
            lj1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            v_sim = True

    if v_sim == False:
        print('')
        print(f'[{x1}]|[{x2}]|[{x3}]')
        print(f'[{x4}]|[{x5}]|[{x6}]')
        print(f'[{x7}]|[{x8}]|[{x9}]')
        print('')
        print('Selecione um numero:')
        pl1 = input_int("> ")
        print('')
        for i,i1 in zip(lj1,lc1):
            if i == pl1 and i1 == pl1:
                posicao = lj1.index(pl1)
                lj1[posicao] = s_p1
            elif i != pl1 and i1 == pl1:
                ps2 = corrigir()
                posicao = lj1.index(ps2)
                lj1[posicao] = s_p1

    x1, x2, x3, x4, x5, x6, x7, x8, x9 = lj1[0], lj1[1], lj1[2], lj1[3], lj1[4], lj1[5], lj1[6], lj1[7], lj1[8]
    v1 = ver_vitoria()
    v2 = verificar()

    if v2 == False:
        finalizar()
        espacar()
        c1 = perguntar()
        if c1 == False:
            break
        else:
            lj1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            v_sim = True

    elif v1 == f'{f_ciano()}Player {f_amarelo()}Wins{f_reset()}':
        espacar()
        print('')
        print(v1)
        print('')
        print(f'[{x1}]|[{x2}]|[{x3}]')
        print(f'[{x4}]|[{x5}]|[{x6}]')
        print(f'[{x7}]|[{x8}]|[{x9}]')
        print('')
        print('Aperte a tecla [ENTER] para continuar:')
        input('> ')
        espacar()
        c1 = perguntar()
        if c1 == False:
            break
        else:
            lj1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            v_sim = True

    elif v1 == f'{f_vermelho()}CPU {f_amarelo()}Wins{f_reset()}':
        espacar()
        print('')
        print(v1)
        print('')
        print(f'[{x1}]|[{x2}]|[{x3}]')
        print(f'[{x4}]|[{x5}]|[{x6}]')
        print(f'[{x7}]|[{x8}]|[{x9}]')
        print('')
        print('Aperte a tecla [ENTER] para continuar:')
        input('> ')
        espacar()
        c1 = perguntar()
        if c1 == False:
            break
        else:
            lj1 = [1,2,3,4,5,6,7,8,9]
            v_sim = True

    if v_sim == False:
        for i,i1 in zip(lj1,lc1):
            if i == numr1 and i1 == numr1:
                posicao = lj1.index(i)
                lj1[posicao] = s_c1
            elif i != numr1 and i1 == numr1:
                pc2 = corrigir_cpu()
                posicao = lj1.index(pc2)
                lj1[posicao] = s_c1

