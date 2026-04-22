from random import randint
from ferramentas.inputs import *
from ferramentas.cor import *

pw1 = 0
pl1 = 0

def espaco():
    for i in range(35):
        print('')

def introduzir():
    while True:
        print(f'{negrito()}')
        print(
            f"""
                ░█████                    ░██     ░██                               ░█████████             
                  ░██                     ░██    ░██                                ░██     ░██            
                  ░██   ░███████          ░██   ░██    ░███████  ░████████          ░██     ░██  ░███████  
                  ░██  ░██    ░██ ░██████ ░███████    ░██    ░██ ░██    ░██ ░██████ ░█████████  ░██    ░██ 
            ░██   ░██  ░██    ░██         ░██   ░██   ░█████████ ░██    ░██         ░██         ░██    ░██ 
            ░██   ░██  ░██    ░██         ░██    ░██  ░██        ░██    ░██         ░██         ░██    ░██ 
             ░██████    ░███████          ░██     ░██  ░███████  ░██    ░██         ░██          ░███████  
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

def ver_placar():
    espaco()
    print("")
    print(f"{f_amarelo()}Placar{f_reset()}:")
    print("")
    print(f"{f_verde()}Vitorias{f_reset()}: {pw1}")
    print(f"{f_vermelho()}Derrotas{(f_reset())}: {pl1}")
    continuar()
    espaco()

w1 = introduzir()
while w1:
    espaco()
    r1 = randint(1, 3)
    print(f"{negrito()}")
    print("Escolha:")
    print("")
    print(f"[1] Pedra 🪨")
    print(f"[2] Papel 📄")
    print(f"[3] Tesoura ✂️")
    print(f"[4] {f_amarelo()}Placar{f_reset()}")
    print(f'[0]{f_vermelho()} Sair {f_reset()}')
    print("")
    esc1 = input_int("> ")
    print("")
    if esc1 == 1:
        if r1 == 1:
            print('')
            print('Player: 🪨')
            print('CPU: 🪨')
            print('')
            print('Empate')
            print('')
            continuar()
        elif r1 == 2:
            print('')
            print('Player: 🪨')
            print('CPU: 📄')
            print('')
            print(f'Player {f_azul()}LOSE{f_reset()}')
            print('')
            continuar()
            pl1 += 1
        else:
            print('')
            print('Player: 🪨')
            print('CPU: ✂️')
            print('')
            print(f'Player {f_amarelo()}WINS{f_reset()}')
            print('')
            continuar()
            pw1 += 1

    elif esc1 == 2:
        if r1 == 1:
            print('')
            print('Player: 📄')
            print('CPU: 🪨')
            print('')
            print(f'Player {f_amarelo()}WINS{f_reset()}')
            print('')
            continuar()
            pw1 += 1
        elif r1 == 2:
            print('')
            print('Player: 📄')
            print('CPU: 📄')
            print('')
            print('Empate')
            print('')
            continuar()
        else:
            print('')
            print('Player: 📄')
            print('CPU: ✂️')
            print('')
            print(f'Player {f_azul()}LOSE{f_reset()}')
            print('')
            continuar()
            pl1 += 1

    elif esc1 == 3:
        if r1 == 1:
            print('')
            print('Player: ✂️')
            print('CPU: 🪨')
            print('')
            print(f'Player {f_azul()}LOSE{f_reset()}')
            print('')
            continuar()
            pl1 += 1
        elif r1 == 2:
            print('')
            print('Player: ✂️')
            print('CPU: 📄')
            print('')
            print(f'Player {f_amarelo()}WINS{f_reset()}')
            print('')
            continuar()
            pw1 += 1
        else:
            print('')
            print('Player: ✂️')
            print('CPU: ✂️')
            print('')
            print('Empate')
            print('')
            continuar()

    elif esc1 == 4:
        ver_placar()

    elif esc1 == 0:
        break


            
