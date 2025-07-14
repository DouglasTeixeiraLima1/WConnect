# WConnect - Tradutor de Textos com Deep Translator

O **WConnect** é uma aplicação simples para tradução de textos entre diferentes idiomas utilizando a biblioteca `deep_translator`. Ele permite que o usuário insira uma mensagem e escolha para qual idioma deseja traduzi-la. O código automaticamente detecta o idioma original da mensagem e realiza a tradução para o idioma selecionado.

## Tecnologias Usadas

- **Python** 3.x
- **deep_translator**: Biblioteca para tradução de textos utilizando o Google Translator e outros serviços.
- **unidecode**: Biblioteca para remover acentos dos caracteres, facilitando a busca por idiomas.

## Funcionalidades

- Tradução automática entre vários idiomas.
- Interface simples via terminal.
- Suporte para mais de 20 idiomas, incluindo inglês, espanhol, francês, alemão, russo, japonês e muitos mais.

## Como Usar

### Pré-requisitos

1. **Python 3.x** instalado.
2. Instalar as bibliotecas necessárias:
   
   ```bash
   pip install deep-translator unidecode


Como Rodar

1° Clone o repositório ou baixe o código.
    git clone git clone https://github.com/DouglasTeixeiraLima1/WConnect.git

2° Execute o script Python:
    python wconnect.py

3° O programa solicitará que você insira a mensagem a ser traduzida e o idioma para o qual deseja traduzir a mensagem. Escolha um dos idiomas suportados (como "portugues-br", "ingles", "espanhol", etc.).

4° O programa irá traduzir automaticamente a mensagem para o idioma selecionado e exibir o resultado no terminal.


Idiomas Suportados

O WConnect oferece suporte a uma ampla gama de idiomas:

    Russo (ru)

    Português (Brasil) (pt)

    Inglês (en)

    Espanhol (es)

    Italiano (it)

    Alemão (de)

    Francês (fr)

    Japonês (ja)

    Árabe (ar)

    Chinês (zh)

    Grego (el)

    Islandês (is)

    Hebraico (iw)

    Coreano (ko)

    Norueguês (no)

    Ucraniano (uk)

    Holandês (nl)

    Esperanto (eo)

    Finlandês (fi)

    Galego (gl)

    Indonésio (id)

    Polonês (pl)

    Hindi (hi)

    Latim (la)

    Luxemburguês (lb)

    Turcomeno (tk)

Como Funciona

    O programa solicita ao usuário a mensagem a ser traduzida.

    O usuário escolhe o idioma de destino (o nome do idioma é inserido em formato texto, sem acentos ou espaços).

    O script detecta automaticamente o idioma da mensagem e utiliza a biblioteca deep_translator para realizar a tradução.

    A tradução é exibida no terminal.

Exemplo de Uso

Mensagem:
Olá, como você está?

Digite o idioma que você quer ler:
ingles

Mensagem:
Hello, how are you?
