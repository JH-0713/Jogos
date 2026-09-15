from colorama import Fore,Back,Style
# fonte
def f_vermelho():
    return Fore.RED
def f_verde():
    return Fore.GREEN
def f_amarelo():
    return Fore.YELLOW
def f_azul():
    return Fore.BLUE
def f_cinza():
    return Fore.WHITE
def f_preto():
    return Fore.BLACK
def f_rosa():
    return Fore.MAGENTA
def f_ciano():
    return Fore.CYAN
def f_reset():
    return Fore.RESET

# background
def b_vermelho():
    return Back.RED
def b_verde():
    return Back.GREEN
def b_amarelo():
    return Back.YELLOW
def b_azul():
    return Back.BLUE
def b_cinza():
    return Back.WHITE
def b_preto():
    return Back.BLACK
def b_rosa():
    return Back.MAGENTA
def b_ciano():
    return Back.CYAN
def b_reset():
    return Back.RESET

# estilo
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

# print(f'''
# Fontes:
#
# {f_vermelho()}Vermelho
# {f_verde()}Verde
# {f_amarelo()}Amarelo
# {f_azul()}Azul
# {f_cinza()}Cinza
# {f_preto()}Preto
# {f_rosa()}Rosa
# {f_ciano()}Ciano
# {f_reset()}Voltar
#
# Backgrounds:
#
# {b_vermelho()}Vermelho
# {b_verde()}Verde
# {b_amarelo()}Amarelo
# {b_azul()}Azul
# {b_cinza()}Cinza
# {b_preto()}Preto
# {b_rosa()}Rosa
# {b_ciano()}Ciano
# {b_reset()}Voltar
#
# Tipos:
#
# {s_dim()}Estilo Dim
# {normal()}Estilo Normal
# {negrito()}Estilo Negrito
# {reset_all()}Reset TUDO
#
# ''')