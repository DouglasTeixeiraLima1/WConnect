from deep_translator import GoogleTranslator 
from unidecode import unidecode

#Texto para ser traduzido
texto = input("Mensagem:\n") 

#Dicionário de idiomas(Dict)
mapa_idiomas = {
    "russo": "ru",
    "portugues-br": "pt",
    "ingles": "en",
    "espanhol": "es",
    "italiano": "it",
    "alemao": "de",
    "frances": "fr",
    "japones": "ja",
    "arabe": "ar",
    "chines":"zh",
    "grego":"el",
    "islandes":"is",
    "hebraico":"iw",
    "coreano":"ko",
    "noruegues":"no",
    "ucraniano":"uk"
}

escolha = True
while escolha:
    nome = input("Digite o idioma que você quer ler:\n").lower()
    nome_sem_acento = unidecode(nome)
    if nome_sem_acento in mapa_idiomas:
        target = mapa_idiomas[nome_sem_acento] 
        escolha = False
    else:
        print("Idioma não encontrado! Tente novamente.")
        #teste 
        print(nome_sem_acento)

#identifica idioma de origem do texto e traduz para o idioma desejado
tradutor = GoogleTranslator(Source ="auto", target= target)

#Variável de suporte com o parâmetro para a tradução
traducao = tradutor.translate(texto)
print(f"Mensagem:\n{traducao}")
