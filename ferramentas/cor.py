from colorama import Fore,Back,Style

def f_vermelho():
    return Fore.RED
def f_verde():
    return Fore.GREEN
def f_amarelo():
    return Fore.YELLOW
def f_azul():
    return Fore.BLUE
def f_branco():
    return Fore.WHITE
def f_preto():
    return Fore.BLACK
def f_rosa():
    return Fore.MAGENTA
def f_ciano():
    return Fore.CYAN
def f_reset():
    return Fore.RESET

def b_vermelho():
    return Back.RED
def b_verde():
    return Back.GREEN
def b_amarelo():
    return Back.YELLOW
def b_azul():
    return Back.BLUE
def b_branco():
    return Back.WHITE
def b_preto():
    return Back.BLACK
def b_rosa():
    return Back.MAGENTA
def b_ciano():
    return Back.CYAN
def b_reset():
    return Back.RESET

def s_dim():
    return Style.DIM
def normal():
    return Style.NORMAL
def negrito():
    return Style.BRIGHT
def reset_all():
    return Style.RESET_ALL

def continuar():
    print(f'{negrito()}')
    print(f'Clique em [{f_verde()}ENTER{f_reset()}] para continuar:')
    input("> ")
    print('')