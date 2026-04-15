from ferramentas.inputs import *
from ferramentas.cor import *
from random import randint
from time import sleep

p_pw1 = 0
p_pl1 = 0

def espaco():
    for i in range(35):
        print('')

def introduzir():
    while True:
        print(f"{negrito()}")
        print(f"""
                                                                                                                           {f_amarelo()}█{f_reset()}
                                                                                                                          {f_amarelo()}█ █{f_reset()}
                                                                                                                    {f_amarelo()}█    █ {f_vermelho()}■{f_amarelo()} █    █{f_reset()}
                                                                                                                   {f_amarelo()}█ █  █  █  █  █ █{f_reset()}
                      ░██████                                       ░██    ░██                     ░██████         {f_amarelo()}█████████████████{f_reset()}
                     ░██   ░██                                      ░██    ░██                    ░██   ░██        {f_amarelo()}█████████████████{f_reset()}
                    ░██         ░██████   ░██░████  ░██████         ░██    ░██  ░███████        ░██         ░███████  ░██░████  ░███████   ░██████
                    ░██              ░██  ░███           ░██        ░██    ░██ ░██              ░██        ░██    ░██ ░███     ░██    ░██       ░██
                    ░██         ░███████  ░██       ░███████         ░██  ░██   ░███████        ░██        ░██    ░██ ░██      ░██    ░██  ░███████
                     ░██   ░██ ░██   ░██  ░██      ░██   ░██          ░██░██          ░██        ░██   ░██ ░██    ░██ ░██      ░██    ░██ ░██   ░██
                      ░██████   ░█████░██ ░██       ░█████░██          ░███     ░███████          ░██████   ░███████  ░██       ░███████   ░█████░██
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

def jogar_moeda():
    print("")
    for i in range(6):
        print(f"{f_amarelo()}🪙{f_reset()}")
        sleep(0.5)
        print(f"{f_amarelo()}——{f_reset()}")
        sleep(0.5)
    espaco()
    print(f'{f_amarelo()}🪙{f_reset()}')
    sleep(0.3)
    print('✋')
    sleep(1)
    espaco()
    print('✊')
    sleep(1)
    espaco()

def ver_placar():
    print("")
    print(f"{f_amarelo()}Placar{f_reset()}:")
    print("")
    print(f"{f_verde()}Vitorias{f_reset()}: {p_pw1}")
    print(f"{f_vermelho()}Derrotas{(f_reset())}: {p_pl1}")
    print('')
    print(f'Clique em {f_verde()}[ENTER]{f_reset()} para continuar:')
    input("> ")
    espaco()

w1 = introduzir()
while w1:
    # 1 = cara | 2 = coroa
    moeda = randint(1,10)
    print(f"{negrito()}")
    print("Escolha:")
    print("")
    print("[1] Cara")
    print("[2] Coroa")
    print(f"[3] {f_amarelo()}Placar{f_reset()}")
    print(f"[0] {f_vermelho()}Sair{f_reset()}")
    print("")
    esc1 = input_int("> ")
    print("")
    if esc1 == 1:
        jogar_moeda()
        if moeda <= 5:
            print("Cara")
            print(f'{f_azul()}Player {f_amarelo()}Wins{f_reset()}')
            p_pw1 += 1
        else:
            print("Coroa")
            print(f'{f_azul()}Player {f_vermelho()}Lose{f_reset()}')
            p_pl1 += 1
        print('')
        print(f'Clique em {f_verde()}[ENTER]{f_reset()} para continuar:')
        input("> ")
        espaco()

    elif esc1 == 2:
        jogar_moeda()
        if moeda <= 5:
            print("Coroa")
            print(f'{f_azul()}Player {f_vermelho()}Lose{f_reset()}')
            p_pl1 += 1
        else:
            print("Cara")
            print(f'{f_azul()}Player {f_amarelo()}Wins{f_reset()}')
            p_pw1 += 1
        print('')
        print(f'Clique em {f_verde()}[ENTER]{f_reset()} para continuar:')
        input("> ")
        espaco()

    elif esc1 == 3:
        ver_placar()

    elif esc1 == 0:
        print('Obrigado por jogar!')
        break
