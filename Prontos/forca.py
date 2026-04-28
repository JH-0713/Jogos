from random import randint
from ferramentas.inputs import *
from ferramentas.cor import *

# Contangem:
c_e1 = 0
verific = False

# Listas:
temas = ['Animal', 'Comida', 'Pais', 'Objeto']

p_animal = [
    "Leão", "Tigre", "Elefante", "Girafa", "Zebra", "Cavalo", "Vaca", "Boi", "Ovelha", "Cabra",
    "Cachorro", "Gato", "Coelho", "Rato", "Camundongo", "Morcego", "Urso", "Lobo", "Raposa", "Hiena",
    "Onça", "Leopardo", "Guepardo", "Canguru", "Coala", "Diabo-da-tasmânia", "Ornitorrinco", "Panda",
    "Búfalo", "Rinoceronte", "Hipopótamo", "Doninha", "Furão", "Texugo", "Esquilo", "Castor",
    "Marmota", "Chimpanzé", "Gorila", "Orangotango", "Macaco", "Lêmure", "Anta", "Tatu", "Tamanduá",
    "Preguiça", "Foca", "Leão-marinho", "Morsa", "Baleia", "Golfinho", "Tubarão", "Polvo", "Lula",
    "Caranguejo", "Lagosta", "Camarão", "Água-viva", "Estrela-do-mar", "Cavalo-marinho", "Pinguim",
    "Águia", "Falcão", "Coruja", "Papagaio", "Arara", "Tucano", "Pardal", "Pombo", "Flamingo",
    "Garça", "Cisne", "Galo", "Galinha", "Peru", "Codorna", "Jacaré", "Crocodilo", "Lagarto",
    "Camaleão", "Iguana", "Cobra", "Salamandra", "Sapo", "Rã", "Perereca", "Peixe-palhaço",
    "Tilápia", "Salmão", "Atum", "Sardinha", "Bicho-preguiça", "Besouro", "Borboleta", "Mariposa",
    "Formiga", "Abelha", "Vespa", "Gafanhoto"
]

p_comida = [
    "Arroz", "Feijão", "Macarrão", "Lasanha", "Pizza", "Hambúrguer", "Cachorro-quente", "Sushi",
    "Sashimi", "Temaki", "Yakissoba", "Risoto", "Nhoque", "Ravioli", "Panqueca", "Omelete",
    "Salada", "Salada Caesar", "Frango grelhado", "Frango frito", "Carne assada", "Bife acebolado",
    "Costela", "Linguiça", "Peixe frito", "Peixe assado", "Camarão empanado", "Moqueca",
    "Feijoada", "Churrasco", "Escondidinho", "Strogonoff", "Purê de batata", "Batata frita",
    "Batata assada", "Farofa", "Cuscuz", "Tapioca", "Pão francês", "Pão de queijo",
    "Croissant", "Sanduíche", "Torrada", "Bolo de chocolate", "Bolo de cenoura", "Cupcake",
    "Brownie", "Brigadeiro", "Beijinho", "Quindim", "Pudim", "Gelatina", "Sorvete",
    "Açaí na tigela", "Milk-shake", "Iogurte", "Queijo", "Presunto", "Mortadela",
    "Salame", "Pastel", "Coxinha", "Kibe", "Empada", "Empadão", "Esfiha",
    "Torta salgada", "Torta doce", "Maçã", "Banana", "Laranja", "Uva",
    "Manga", "Abacaxi", "Melancia", "Melão", "Morango", "Pera",
    "Ameixa", "Pêssego", "Kiwi", "Maracujá", "Acerola", "Goiaba",
    "Chocolate", "Bala", "Chiclete", "Doce de leite", "Rapadura",
    "Canjica", "Arroz doce", "Mingau", "Sopa", "Caldo verde",
    "Feijão tropeiro", "Virado à paulista", "Dobradinha", "Polenta"
]

p_paises = [
    "Brasil", "Argentina", "Chile", "Uruguai", "Paraguai", "Bolívia", "Peru", "Colômbia", "Venezuela", "Equador",
    "Guiana", "Suriname", "México", "Estados Unidos", "Canadá", "Cuba", "Jamaica", "Haiti", "República Dominicana",
    "Panamá",
    "Costa Rica", "Nicarágua", "Honduras", "El Salvador", "Guatemala",
    "Portugal", "Espanha", "França", "Alemanha", "Itália", "Reino Unido", "Irlanda", "Holanda", "Bélgica", "Suíça",
    "Áustria", "Polônia", "República Tcheca", "Eslováquia", "Hungria", "Romênia", "Bulgária", "Grécia", "Noruega",
    "Suécia",
    "Finlândia", "Dinamarca", "Islândia", "Rússia", "Ucrânia",
    "China", "Japão", "Coreia do Sul", "Coreia do Norte", "Índia", "Paquistão", "Bangladesh", "Sri Lanka", "Nepal",
    "Afeganistão",
    "Tailândia", "Vietnã", "Malásia", "Singapura", "Indonésia", "Filipinas",
    "Austrália", "Nova Zelândia",
    "África do Sul", "Egito", "Nigéria", "Quênia", "Etiópia", "Marrocos", "Argélia", "Tunísia", "Gana", "Camarões",
    "Arábia Saudita", "Emirados Árabes Unidos", "Israel", "Turquia", "Irã", "Iraque", "Síria", "Jordânia", "Líbano",
    "Catar",
    "Kuwait", "Omã", "Iêmen","Mongólia",
    "Cazaquistão", "Uzbequistão", "Turcomenistão", "Quirguistão", "Tajiquistão"
]

p_objeto = [
    "Mesa", "Cadeira", "Sofá", "Cama", "Armário", "Estante", "Escrivaninha", "Banco", "Poltrona", "Criado-mudo",
    "Geladeira", "Fogão", "Micro-ondas", "Liquidificador", "Batedeira", "Torradeira", "Cafeteira", "Panela",
    "Frigideira", "Chaleira",
    "Prato", "Copo", "Taça", "Talher", "Garfo", "Faca", "Colher", "Bandeja", "Jarra", "Garrafa",
    "Lápis", "Caneta", "Borracha", "Apontador", "Caderno", "Livro", "Agenda", "Marcador", "Régua", "Estojo",
    "Mochila", "Bolsa", "Carteira", "Chave", "Fechadura", "Cadeado", "Relógio", "Óculos", "Espelho", "Pente",
    "Escova", "Secador", "Toalha", "Sabonete", "Shampoo", "Condicionador", "Perfume", "Desodorante", "Barbeador",
    "Esponja",
    "Vassoura", "Rodo", "Balde", "Pá", "Aspirador", "Pano", "Detergente", "Sabão", "Lixeira", "Cesto",
    "Televisão", "Controle", "Computador", "Notebook", "Teclado", "Mouse", "Monitor", "Impressora", "Tablet", "Celular",
    "Carregador", "Fone de ouvido", "Caixa de som", "Câmera", "Tripé", "Drone", "Pendrive", "HD", "Roteador",
    "Modem",
    "Ventilador", "Ar-condicionado", "Aquecedor", "Lâmpada", "Abajur", "Lanterna", "Interruptor", "Tomada", "Extensão",
    "Bateria"
]

mamiferos = [
    "Leão", "Tigre", "Elefante", "Girafa", "Zebra", "Cavalo", "Vaca", "Boi",
    "Ovelha", "Cabra", "Cachorro", "Gato", "Coelho", "Rato", "Camundongo",
    "Morcego", "Urso", "Lobo", "Raposa", "Hiena", "Onça", "Leopardo",
    "Guepardo", "Canguru", "Coala", "Diabo-da-tasmânia", "Ornitorrinco",
    "Panda", "Búfalo", "Rinoceronte", "Hipopótamo", "Doninha", "Furão",
    "Texugo", "Esquilo", "Castor", "Marmota", "Chimpanzé", "Gorila",
    "Orangotango", "Macaco", "Lêmure", "Anta", "Tatu", "Tamanduá",
    "Preguiça", "Foca", "Leão-marinho", "Morsa", "Baleia", "Golfinho"
]

aves = [
    "Pinguim", "Águia", "Falcão", "Coruja", "Papagaio", "Arara",
    "Tucano", "Pardal", "Pombo", "Flamingo", "Garça", "Cisne",
    "Galo", "Galinha", "Peru", "Codorna"
]

repteis = [
    "Jacaré", "Crocodilo", "Lagarto", "Camaleão", "Iguana", "Cobra"
]

anfibios = [
    "Salamandra", "Sapo", "Rã", "Perereca"
]

marinhos = [
    "Tubarão", "Peixe-palhaço", "Tilápia", "Salmão", "Atum", "Sardinha",
    "Polvo", "Lula", "Caranguejo", "Lagosta", "Camarão", "Água-viva",
    "Estrela-do-mar", "Cavalo-marinho"
]

insetos = [
    "Besouro", "Borboleta", "Mariposa",
    "Formiga", "Abelha", "Vespa", "Gafanhoto"
]

pratos_principais = [
    "Lasanha", "Pizza", "Hambúrguer", "Cachorro-quente",
    "Sushi", "Sashimi", "Temaki", "Yakissoba",
    "Risoto", "Nhoque", "Ravioli", "Panqueca",
    "Moqueca", "Feijoada", "Churrasco",
    "Escondidinho", "Strogonoff",
    "Sopa", "Caldo verde",
    "Feijão tropeiro", "Virado à paulista",
    "Dobradinha",
    "Salada", "Salada Caesar", "Batata frita"
]

frutas = [
    "Maçã", "Banana", "Laranja", "Uva", "Manga",
    "Abacaxi", "Melancia", "Melão", "Morango",
    "Pera", "Ameixa", "Pêssego", "Kiwi",
    "Maracujá", "Acerola", "Goiaba"
]

lanches = [
    "Sanduíche", "Pastel", "Coxinha",
    "Empada", "Empadão", "Esfiha",
    "Torta salgada"
]

doces = [
    "Bolo de chocolate", "Bolo de cenoura", "Cupcake",
    "Brownie", "Brigadeiro", "Beijinho", "Quindim",
    "Pudim", "Gelatina", "Sorvete",
    "Açaí na tigela", "Milk-shake", "Iogurte",
    "Torta doce", "Chocolate", "Bala", "Chiclete",
    "Doce de leite", "Rapadura", "Canjica",
    "Arroz doce", "Mingau"
]

america_sul = [
    "Brasil", "Argentina", "Chile", "Uruguai", "Paraguai",
    "Bolívia", "Peru", "Colômbia", "Venezuela", "Equador",
    "Guiana", "Suriname"
]

america_norte = [
    "Estados Unidos", "Canadá", "México"
]

america_central = [
    "Guatemala", "Belize", "Honduras", "El Salvador",
    "Nicarágua", "Costa Rica", "Panamá",
    "Cuba", "Jamaica", "Haiti", "República Dominicana"
]

europa = [
    "Portugal", "Espanha", "França", "Alemanha", "Itália",
    "Reino Unido", "Irlanda", "Holanda", "Bélgica", "Suíça",
    "Áustria", "Polônia", "República Tcheca", "Eslováquia",
    "Hungria", "Romênia", "Bulgária", "Grécia",
    "Noruega", "Suécia", "Finlândia", "Dinamarca",
    "Islândia", "Rússia", "Ucrânia"
]

asia = [
    "China", "Japão", "Coreia do Sul", "Coreia do Norte",
    "Índia", "Paquistão", "Bangladesh", "Sri Lanka", "Nepal",
    "Afeganistão", "Tailândia", "Vietnã", "Malásia",
    "Singapura", "Indonésia", "Filipinas",
    "Arábia Saudita", "Emirados Árabes Unidos", "Israel",
    "Turquia", "Irã", "Iraque", "Síria", "Jordânia",
    "Líbano", "Catar", "Kuwait", "Omã", "Iêmen",
    "Cazaquistão", "Uzbequistão", "Turcomenistão",
    "Quirguistão", "Tajiquistão","Mongólia"
]

africa = [
    "África do Sul", "Egito", "Nigéria", "Quênia",
    "Etiópia", "Marrocos", "Argélia", "Tunísia",
    "Gana", "Camarões"
]

oceania = [
    "Austrália", "Nova Zelândia"
]


sala = [
    "Sofá", "Poltrona", "Mesa", "Cadeira",
    "Estante", "Televisão", "Controle",
    "Caixa de som", "Tapete"
]

quarto = [
    "Cama", "Armário", "Criado-mudo",
    "Escrivaninha", "Cadeira",
    "Relógio", "Espelho", "Abajur",
    "Mochila", "Bolsa", "Carteira"
]

cozinha = [
    "Geladeira", "Fogão", "Micro-ondas",
    "Liquidificador", "Batedeira", "Torradeira",
    "Cafeteira", "Panela", "Frigideira", "Chaleira",
    "Prato", "Copo", "Taça", "Talher",
    "Garfo", "Faca", "Colher",
    "Bandeja", "Jarra", "Garrafa"
]

banheiro = [
    "Toalha", "Sabonete", "Shampoo",
    "Condicionador", "Perfume",
    "Desodorante", "Barbeador",
    "Pente", "Escova"
]

limpeza = [
    "Vassoura", "Rodo", "Balde", "Pá",
    "Aspirador", "Pano", "Esponja",
    "Detergente", "Sabão", "Lixeira", "Cesto"
]

escritorio = [
    "Lápis", "Caneta", "Borracha", "Apontador",
    "Caderno", "Livro", "Agenda",
    "Marcador", "Régua", "Estojo",
    "Computador", "Notebook", "Teclado",
    "Mouse", "Monitor", "Impressora",
    "Tablet", "Celular", "Carregador"
]

tecnologia = [
    "Fone de ouvido", "Caixa de som",
    "Câmera", "Tripé", "Drone",
    "Pendrive", "HD",
    "Roteador", "Modem",
    "Interruptor", "Tomada", "Extensão",
    "Bateria","Ventilador", "Ar-condicionado", "Aquecedor",
    "Lâmpada", "Lanterna"
]

def continuar():
    print(f'{negrito()}')
    print(f'Clique em [{f_verde()}ENTER{f_reset()}] para continuar:')
    input("> ")
    print('')
    global verific
    verific = True

def perguntar():
    while True:
        print(f"{negrito()}")
        print(f"Deseja continuar? [{f_verde()}S{f_reset()}/{f_vermelho()}N{f_reset()}]")
        print("")
        ex1 = input_str("> ").upper()
        print("")
        if ex1 == "S" or ex1 == "SI" or ex1 == "SIM":
            print("Ok Selecionando outro Numero...")
            print('')
            espaco()
            return True
        elif ex1 == "N" or ex1 == "NA" or ex1 == "NÃ" or ex1 == "NAO" or ex1 == "NÃO":
            print('Saindo do Jogo...')
            return False
        else:
            pass

# Seleciona a Palavra
def selecionar_tema(tema):
    tema = tema.upper()
    if tema == "ANIMAL":
        p1 = randint(1, 100) - 1
        return p_animal[p1]
    elif tema == "COMIDA":
        p1 = randint(1, 96) - 1
        return p_comida[p1]
    elif tema == "PAIS":
        p1 = randint(1, 99) - 1
        return p_paises[p1]
    elif tema == "OBJETO":
        p1 = randint(1, 98) - 1
        return p_objeto[p1]

# Escolha de Tema
def escolher_tema():
    while True:
        print(f'{negrito()}')
        print('')
        print(f'[1] {f_vermelho()}Animais{f_reset()}')
        print(f'[2] {f_verde()}Comida{f_reset()}')
        print(f'[3] {f_amarelo()}Paises{f_reset()}')
        print(f'[4] {f_ciano()}Objeto{f_reset()}')
        print('')
        esc1 = input_int('> ')
        new_esc = esc1 - 1
        print('')
        if not esc1 > len(temas) or not esc1 < len(temas):
            t1 = temas[new_esc]
            palavra1 = selecionar_tema(t1)
            return t1, palavra1
        else:
            pass

# Definir Tipo
def definir_tipo(pala1):
    if te1 == "Animal":
        if pala1 in mamiferos:
            return 'Mamifero'
        elif pala1 in aves:
            return 'Ave'
        elif pala1 in repteis:
            return 'Reptei'
        elif pala1 in anfibios:
            return 'Anfibio'
        elif pala1 in marinhos:
            return 'Marinho'
        elif pala1 in insetos:
            return 'Insetos'
    if te1 == "Comida":
        if pala1 in pratos_principais:
            return 'Refeições'
        elif pala1 in frutas:
            return 'Frutas'
        elif pala1 in doces:
            return 'Doces'
        elif pala1 in lanches:
            return 'Lanches'
    if te1 == "Pais":
        if pala1 in america_sul:
            return 'America do Sul'
        elif pala1 in america_central:
            return 'America Central'
        elif pala1 in america_norte:
            return 'America Norte'
        elif pala1 in europa:
            return 'Europa'
        elif pala1 in asia:
            return 'Ásia'
        elif pala1 in africa:
            return 'África'
        elif pala1 in oceania:
            return 'Oceania'
    if te1 == "Objeto":
        if pala1 in sala:
            return 'Sala'
        elif pala1 in quarto:
            return 'Quarto'
        elif pala1 in cozinha:
            return 'Cozinha'
        elif pala1 in banheiro:
            return 'Banheiro'
        elif pala1 in limpeza:
            return 'Limpeza'
        elif pala1 in escritorio:
            return 'Escritório'
        elif pala1 in tecnologia:
            return 'Tecnologia'

def enforcar(es1):
    if es1 == 0:
        f0 = '''
░████████████████                                       
░██                                                 
░██             
░██ 
░██ 
░██        
░██ '''
        return f0
    elif es1 == 1:
        f1 = '''
░████████████████                                       
░██            ░                                    
░██            ■
░██ 
░██ 
░██        
░██ '''
        return f1
    elif es1 == 2:
        f2 = '''
░████████████████                                       
░██            ░                                    
░██            ■
░██            |
░██ 
░██        
░██ '''
        return f2
    elif es1 == 3:
        f3 = '''
░████████████████                                       
░██            ░                                    
░██            ■
░██            |\\
░██ 
░██        
░██ '''
        return f3
    elif es1 == 4:
        f4 = '''
░████████████████                                       
░██            ░                                    
░██            ■
░██           /|\\
░██             
░██        
░██ '''
        return f4
    elif es1 == 5:
        f5 = '''
░████████████████                                       
░██            ░                                    
░██            ■
░██           /|\\
░██             \\
░██        
░██ '''
        return f5
    elif es1 == 6:
        f6 = '''
░████████████████                                       
░██            ░                                    
░██            ■
░██           /|\\
░██           / \\
░██        
░██ '''
        return f6
    elif es1 == 7:
        f7 = f'''
░████████████████                                       
░██            ░                                    
░██            {f_vermelho()}■{f_reset()}
░██           /|\\
░██           / \\
░██        
░██ '''
        return f7
    else:
        return 'Valor não encontrados'

def espaco():
    for i in range(35):
        print('')

def introduzir():
    while True:
        print(f'{negrito()}')
        print(
            f"""
    ░████████████████                                       
    ░██             ░                                    
    ░██         ░███████  ░██░████  ░███████   ░██████   
    ░█████████ ░██  {f_vermelho()}■{f_reset()} ░██ ░███     ░██    ░██       ░██  
    ░██        ░██ /|\\░██ ░██      ░██         ░███████  
    ░██        ░██ / \░██ ░██      ░██    ░██ ░██   ░██  
    ░██         ░███████  ░██       ░███████   ░█████░██ 
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

def corrigir(c1):
    cara1 = c1.lower()

    if cara1 in "áàãâ":
        return "a"
    if cara1 in "éê":
        return "e"
    if cara1 == "í":
        return "i"
    if cara1 in "óôõ":
        return "o"
    if cara1 == "ú":
        return "u"
    if cara1 == "ç":
        return "c"

    return cara1

def atualizar_jogo(pa1, pa_jogo, l1):
    vitoria = False
    letra_1 = corrigir(l1)
    for i in range(len(pa1)): # Faz a contagem de vezes de que deu o loop
        if corrigir(pa1[i]) == letra_1:
            pa_jogo[i] = pa1[i]
            vitoria = True

    return vitoria

w1 = introduzir()

if w1 == True:
    te1, palav1 = escolher_tema()
    l_pa1 = list(palav1)
    l_jogo = []
    for i in range(len(l_pa1)):
        if l_pa1[i] == '-':
            l_jogo.append('-')
        elif l_pa1[i] == ' ':
            l_jogo.append('-')
        else:
            l_jogo.append('__')
    tip1 = definir_tipo(palav1)
    l_caracteres = []
    espaco()

while w1:
    print(f'{negrito()}')
    if c_e1 >= 7:
        print(enforcar(c_e1))
        print("")
        print(f"Você {f_vermelho()}perdeu{f_reset()}!")
        print("")
        print("Palavra era:", palav1)
        continuar()

    if "__" not in l_jogo:
        espaco()
        print(enforcar(c_e1), *[i for i in l_jogo])
        print("")
        print(f"Você {f_amarelo()}ganhou{f_reset()}!")
        print("")
        print("Palavra era:", palav1)
        continuar()

    if verific == True:
        espaco()
        w1 = perguntar()
        verific = False
        if w1 == True:
            te1, palav1 = escolher_tema()
            l_pa1 = list(palav1)
            l_jogo = []
            c_e1 = 0
            for i in range(len(l_pa1)):
                if l_pa1[i] == '-':
                    l_jogo.append('-')
                elif l_pa1[i] == ' ':
                    l_jogo.append('-')
                else:
                    l_jogo.append('__')
            tip1 = definir_tipo(palav1)
            l_caracteres = []

    if w1 == True:
        print("")
        print(f"Tema: {te1}")
        print(f"Tipo: {tip1}")
        print('Letras já selecionadas:',*[i for i in l_caracteres])
        print("")
        print(enforcar(c_e1),*[i for i in l_jogo])
        print("")
        exc1 = input_str("> ")
        print("")
        if exc1 in l_caracteres:
            print('Letra já selecionada')
            pass
        else:
            espaco()
            if atualizar_jogo(l_pa1,l_jogo,exc1):
                if exc1 in l_caracteres:
                    pass
                else:
                    l_caracteres.append(exc1)
            else:
                c_e1 +=1
                if exc1 in l_caracteres:
                    pass
                else:
                    l_caracteres.append(exc1)