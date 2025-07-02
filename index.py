from deep_translator import GoogleTranslator 

#Texto para ser traduzido
texto = input("Mensagem:\n") 

mapa_idiomas = {
    "russo": "ru",
    "português-br": "pt",
    "inglês": "en",
    "espanhol": "es",
    "italiano": "it",
    "alemão": "de",
    "francês": "fr"
}

escolha = True
while escolha:
    # Pegando o input do usuário
    nome = input("Digite o idioma que você quer ler:\n").lower()
# Verificando se está no dicionário
    if nome in mapa_idiomas:
        target = mapa_idiomas[nome]
        escolha = False
    else:
        print("Nome não encontrado, tente novamente.")


#I.A identificar idioma de origem do texto e traduzir para o idioma desejado
tradutor = GoogleTranslator(Source ="auto", target= target)

traducao = tradutor.translate(texto)
print(f"Mensagem:\n{traducao}")