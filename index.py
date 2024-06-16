import random

ranking = []
# TODO - Ler o ranking do arquivo ranking.txt

embarcacoes = [
    {
      "nome": "Porta-aviões",
      "tamanho": 5,
      "quantidade": 1
    },
    {
      "nome": "Encouraçado",
      "tamanho": 4,
      "quantidade": 2
    },
    {
      "nome": "Contratorpedeiro",
      "tamanho": 3,
      "quantidade": 2
    },
    {
      "nome": "Submarino",
      "tamanho": 1,
      "quantidade": 4
    }
]

municoes = 10
total_embarcacoes = sum((embarcacao["quantidade"] * embarcacao["tamanho"]) for embarcacao in embarcacoes)
embarcacoes_encontradas = 0

tabuleiro_posicionado = [
    [" " for i in range(10)] for j in range(10)
]

tabuleiro_inicial = [
    [" " for i in range(10)] for j in range(10)
]

usuario = {
  "nome": "",
  "pontos": 0
}

def posicionar_embarcacoes_random():
  for embarcacao in embarcacoes:
    for i in range(embarcacao["quantidade"]):
      print(f"Posicione o {embarcacao['nome']} {i + 1}/{embarcacao['quantidade']}")
      while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        direcao = random.choice(["h", "v"])

        if direcao == "h":
          if x + embarcacao["tamanho"] <= len(tabuleiro_posicionado) and all(tabuleiro_posicionado[y][x + j] == " " for j in range(embarcacao["tamanho"])):
            for j in range(embarcacao["tamanho"]):
              tabuleiro_posicionado[y][x + j] = embarcacao["nome"][0]
            break
        else:
          if y + embarcacao["tamanho"] <= len(tabuleiro_posicionado) and all(tabuleiro_posicionado[y + j][x] == " " for j in range(embarcacao["tamanho"])):
            for j in range(embarcacao["tamanho"]):
              tabuleiro_posicionado[y + j][x] = embarcacao["nome"][0]
            break

def imprimir_tabuleiro():
    print("  0 1 2 3 4 5 6 7 8 9")
    for i in range(10):        
      print(str(i) + ' ' + ' '.join(tabuleiro_inicial[i]))

def imprimir_posicoes():
    print("  0 1 2 3 4 5 6 7 8 9")
    for i in range(10):        
      print(str(i) + ' ' + ' '.join(tabuleiro_posicionado[i]))

def ler_usuario():
    usuario["nome"] = input("Qual é o seu nome? ")

def atirar():
    global municoes
    global embarcacoes_encontradas
    
    print(f"Você tem {municoes} munições")

    while True:
      pos_x = input("Digite a coordenada X: ")
      pos_y = input("Digite a coordenada Y: ")
    
      if pos_x.isdigit() and pos_y.isdigit():
        y = int(pos_y)
        x = int(pos_x)
        break;

      print("Coordenadas inválidas")


    if tabuleiro_posicionado[y][x] != " ":
        print("Você acertou!")
        usuario["pontos"] += 1
        municoes += 2
        embarcacoes_encontradas += 1
        tabuleiro_inicial[y][x] = tabuleiro_posicionado[y][x]
    else:
        print("Você errou!")
        municoes -= 1
        tabuleiro_inicial[y][x] = "X"

def salvar_ranking():
  with open('ranking.txt', 'a') as file:
    file.write(f"{usuario['nome']},{usuario['pontos']}\n")

def main():
    ler_usuario()
    posicionar_embarcacoes_random()

    while municoes > 0:
        imprimir_tabuleiro()
        atirar()

    print(f"Você fez {usuario['pontos']} pontos")
    salvar_ranking()
    imprimir_posicoes()

# TODO - Salvar o ranking no arquivo ranking.txt
# TODO - Mostrar o ranking no final do jogo
# TODO - Criar sistema de pontuação
# TODO - Validar quando o usuário acertar todas as embarcações

main()