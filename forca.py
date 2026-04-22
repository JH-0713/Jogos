from random import randint
from ferramentas.inputs import *
from ferramentas.cor import *

# Listas:
temas = ['Animal','Comida','Pais','Objeto']

p_animal =  [
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
    "Guiana", "Suriname", "México", "Estados Unidos", "Canadá", "Cuba", "Jamaica", "Haiti", "República Dominicana", "Panamá",
    "Costa Rica", "Nicarágua", "Honduras", "El Salvador", "Guatemala",
    "Portugal", "Espanha", "França", "Alemanha", "Itália", "Reino Unido", "Irlanda", "Holanda", "Bélgica", "Suíça",
    "Áustria", "Polônia", "República Tcheca", "Eslováquia", "Hungria", "Romênia", "Bulgária", "Grécia", "Noruega", "Suécia",
    "Finlândia", "Dinamarca", "Islândia", "Rússia", "Ucrânia",
    "China", "Japão", "Coreia do Sul", "Coreia do Norte", "Índia", "Paquistão", "Bangladesh", "Sri Lanka", "Nepal", "Afeganistão",
    "Tailândia", "Vietnã", "Malásia", "Singapura", "Indonésia", "Filipinas",
    "Austrália", "Nova Zelândia",
    "África do Sul", "Egito", "Nigéria", "Quênia", "Etiópia", "Marrocos", "Argélia", "Tunísia", "Gana", "Camarões",
    "Arábia Saudita", "Emirados Árabes Unidos", "Israel", "Turquia", "Irã", "Iraque", "Síria", "Jordânia", "Líbano", "Catar",
    "Kuwait", "Omã", "Iêmen",
    "Cazaquistão", "Uzbequistão", "Turcomenistão", "Quirguistão", "Tajiquistão"
]
p_objeto =  [
    "Mesa", "Cadeira", "Sofá", "Cama", "Armário", "Estante", "Escrivaninha", "Banco", "Poltrona", "Criado-mudo",
    "Geladeira", "Fogão", "Micro-ondas", "Liquidificador", "Batedeira", "Torradeira", "Cafeteira", "Panela", "Frigideira", "Chaleira",
    "Prato", "Copo", "Taça", "Talher", "Garfo", "Faca", "Colher", "Bandeja", "Jarra", "Garrafa",
    "Lápis", "Caneta", "Borracha", "Apontador", "Caderno", "Livro", "Agenda", "Marcador", "Régua", "Estojo",
    "Mochila", "Bolsa", "Carteira", "Chave", "Fechadura", "Cadeado", "Relógio", "Óculos", "Espelho", "Pente",
    "Escova", "Secador", "Toalha", "Sabonete", "Shampoo", "Condicionador", "Perfume", "Desodorante", "Barbeador", "Esponja",
    "Vassoura", "Rodo", "Balde", "Pá", "Aspirador", "Pano", "Detergente", "Sabão", "Lixeira", "Cesto",
    "Televisão", "Controle", "Computador", "Notebook", "Teclado", "Mouse", "Monitor", "Impressora", "Tablet", "Celular",
    "Carregador", "Fone de ouvido", "Caixa de som", "Câmera", "Tripé", "Drone", "Pendrive", "HD externo", "Roteador", "Modem",
    "Ventilador", "Ar-condicionado", "Aquecedor", "Lâmpada", "Abajur", "Lanterna", "Interruptor", "Tomada", "Extensão", "Bateria"
]

l_jogo = []

def ver(list1):
    print(len(list1))

# Animal: 100
# Comida: 96
# Pais: 99
# Objeto: 98

def selecionar_tema(tema):
    tema = tema.upper()
    if tema == "ANIMAL":
        return randint(1,100) - 1
    elif tema == "COMIDA":
        return randint(1,96) - 1
    elif tema == "PAIS":
        return randint(1,99) - 1
    elif tema == "OBJETO":
        return randint(1,98) - 1

def escolher_tema():
    while True:
        print('')
        x1 = 0
        for i in temas:
            x1 += 1
            print(f'[{x1}] {i}')
        print('')
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

w1 = introduzir()

te1,palav1 = escolher_tema()



while w1:


