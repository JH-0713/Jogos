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
    print(f"{negrito()}")
    print("""
    
    
                                                                                                                         
                                                                                                                       
                                                                                                                          *
                                                                                                                        * | *
                                                                                                                       * \\|/ *
                                                                                                                  * * * \\|O|/ * * *
                      ░██████                                       ░██    ░██                     ░██████         \\o\\o\\o|O|o/o/o/                  
                     ░██   ░██                                      ░██    ░██                    ░██   ░██        (<><><>O<><><>)                      
                    ░██         ░██████   ░██░████  ░██████         ░██    ░██  ░███████        ░██         ░███████  ░██░████  ░███████   ░██████   
                    ░██              ░██  ░███           ░██        ░██    ░██ ░██              ░██        ░██    ░██ ░███     ░██    ░██       ░██  
                    ░██         ░███████  ░██       ░███████         ░██  ░██   ░███████        ░██        ░██    ░██ ░██      ░██    ░██  ░███████  
                     ░██   ░██ ░██   ░██  ░██      ░██   ░██          ░██░██          ░██        ░██   ░██ ░██    ░██ ░██      ░██    ░██ ░██   ░██  
                      ░██████   ░█████░██ ░██       ░█████░██          ░███     ░███████          ░██████   ░███████  ░██       ░███████   ░█████░██ 
    """)
    print("")
    print('')
    print(f'[1] {f_verde()}Jogar{f_reset()}')
    print(f'[2] Sair')
    print('')
    ex1 = input_int("> ")
    if ex1 == 1:
        espaco()
        return True
    elif ex1 == 2:
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
    print("Placar:")
    print("")
    print(f"Vitorias: {p_pw1}")
    print(f"Derrotas: {p_pl1}")
    print('')
    print('Clique em [ENTER] para continuar:')
    input("> ")

w1 = introduzir()
while w1:
    # 1 = cara | 2 = coroa
    moeda = randint(1,2)
    print(f"{negrito()}")
    print("Escolha:")
    print("")
    print("[1] Cara")
    print("[2] Coroa")
    print("[3] Placar")
    print("[0] Sair")
    print("")
    esc1 = input_int("> ")
    print("")
    jogar_moeda()

    if esc1 == 1:
        if moeda == 1:
            print("Cara")
            print(f'Player {f_amarelo()}Wins{f_reset()}')
        else:
            print("Coroa")
            print(f'Player {f_azul()}Lose{f_reset()}')
        print('')
        print('Clique em [ENTER] para continuar:')
        input("> ")

    elif esc1 == 2:
        if moeda == 1:
            print("Coroa")
            print(f'Player {f_azul()}Lose{f_reset()}')
        else:
            print("Cara")
            print(f'Player {f_amarelo()}Wins{f_reset()}')
        print('')
        print('Clique em [ENTER] para continuar:')
        input("> ")

    elif esc1 == 3:
        ver_placar()

    elif esc1 == 0:
        break
