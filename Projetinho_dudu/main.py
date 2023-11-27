import time
import random
dicionario = {
    "act": ["ato"],
    "apple": ["maçã"],
    "air": ["ar"],
    "animal": ["animal"],
    "baby": ["bebê"],
    "back": ["costas", "parte de trás"],
    "ball": ["bola"],
    "bear": ["urso"],
    "bed": ["cama"],
    "bell": ["sino", "campainha"],
    "bird": ["pássaro"],
    "birthday": ["aniversário"],
    "boat": ["barco"],
    "box": ["caixa"],
    "boy": ["menino"],
    "bread": ["pão"],
    "brother": ["irmão"],
    "cake": ["bolo"],
    "call": ["chamada"],
    "car": ["carro"],
    "cat": ["gato"],
    "cause": ["causa"],
    "chair": ["cadeira"],
    "chicken": ["galinha", "frango"],
    "children": ["crianças"],
    "Christmas": ["Natal"],
    "coat": ["casaco"],
    "corn": ["milho"],
    "cow": ["vaca"],
    "day": ["dia"],
    "dog": ["cachorro"],
    "doll": ["boneca"],
    "door": ["porta"],
    "duck": ["pato"],
    "edge": ["borda", "beira"],
    "egg": ["ovo"],
    "eye": ["olho"],
    "farm": ["fazenda"],
    "farmer": ["fazendeiro"],
    "father": ["pai"],
    "feet": ["pés"],
    "fire": ["fogo"],
    "fish": ["peixe"],
    "floor": ["chão"],
    "flower": ["flor"],
    "form": ["forma", "formato", "formulário"],
    "game": ["jogo"],
    "garden": ["jardim"],
    "girl": ["menina"],
}



random_word = [
    'Abacate', 'Abraço', 'Açaí', 'Acordar', 'Adeus', 'Afiado', 'Alegria', 'Alface', 'Alho', 'Almofada',
    'Amor', 'Amora', 'Anel', 'Anjo', 'Apelido', 'Aperto', 'Arco-íris', 'Areia', 'Aroma', 'Arroz', 'Asa',
    'Atenção', 'Atleta', 'Aveia', 'Azul', 'Bala', 'Banho', 'Banquete', 'Barulho', 'Batata', 'Bebida',
    'Beijo', 'Beleza', 'Bicicleta', 'Biscoito', 'Boa-noite', 'Bolo', 'Bom-dia', 'Boneco', 'Brilho',
    'Brinquedo', 'Brisa', 'Cabelo', 'Cachecol', 'Café', 'Caixa de correio', 'Calor', 'Calçada', 'Calça',
    'Caminho', 'Camiseta', 'Caneca', 'Caneta', 'Canto', 'Carinho', 'Casa', 'Casamento', 'Castanha', 'Céu',
    'Chá', 'Chapéu', 'Cheiro', 'Chocolate', 'Chuva', 'Cigarro', 'Cinto', 'Circo', 'Cobre', 'Colher',
    'Comida', 'Companheiro', 'Confete', 'Coração', 'Corredor', 'Corrente', 'Cozinha', 'Criança', 'Cuidado',
    'Cunhado', 'Curva', 'Dança', 'Decisão', 'Dedo', 'Deitar', 'Dente', 'Desejo', 'Despertador', 'Dicionário',
    'Direção', 'Disco', 'Docinho', 'Doença', 'Dólar', 'Dormir', 'Elegante', 'Elevador', 'Embaixo', 'Embrulho',
    'Encontro', 'Enfeite', 'Engano', 'Envelope', 'Espaço', 'Esperança', 'Esquerda', 'Estação', 'Estrela',
    'Exemplo', 'Experiência', 'Fada', 'Família', 'Fantasia', 'Farinha', 'Fecho', 'Felicidade', 'Ferro',
    'Festa', 'Fio', 'Florista', 'Folha', 'Formiga', 'Fotografia', 'Frango', 'Frase', 'Frente', 'Fruta',
    'Fundo', 'Futuro', 'Gaita', 'Garfo', 'Gelo', 'Gesto', 'Ginástica', 'Goma', 'Gosto', 'Grama', 'Grão',
    'Guarda-chuva', 'Guardanapo', 'Guia', 'Guirlanda', 'Hidrante', 'Hora', 'Igreja', 'Imperador', 'Impulso',
    'Inverno', 'Irmã', 'Janela', 'Jantar', 'Jogo', 'Jornal', 'Juventude', 'Lágrima', 'Laranja', 'Lata',
    'Leite', 'Lenço', 'Leve', 'Líder', 'Limão', 'Lixo', 'Livro', 'Lua', 'Lugar', 'Luta', 'Macaco',
    'Maçã do amor', 'Mala', 'Mamãe', 'Mandioca', 'Manga', 'Manhã', 'Mão', 'Máquina', 'Mar', 'Marcador',
    'Margarina', 'Máscara', 'Massa', 'Meia', 'Mel', 'Menina', 'Menino', 'Mesa', 'Metrô', 'Meu', 'Mimo',
    'Mola', 'Molho', 'Montanha', 'Mordida', 'Mosaico', 'Mulher', 'Mundo', 'Museu', 'Música', 'Nariz',
    'Neve', 'Noite'
]

while True:
    for x, y in dicionario.items():
        print(f'Qual a tradução da palavra: {x}')
        print(f'{random.choice(random_word)}\n{random.choice(random_word)}\n')
        time.sleep(2)