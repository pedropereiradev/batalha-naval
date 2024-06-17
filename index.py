import random

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

def jogar():
    ler_usuario()
    posicionar_embarcacoes_random()

    while municoes > 0:
      imprimir_tabuleiro()
      atirar()

    print(f"Você fez {usuario['pontos']} pontos")
    salvar_ranking()
    imprimir_posicoes()

def titulo(texto):
  print()
  print(texto)
  print("="*40)

def ranking():
  titulo('Ranking Batalha naval')
  with open('ranking.txt', 'r') as file:
    ranking = file.readlines()
    ranking = [linha.strip() for linha in ranking]
    ranking = [linha.split(',') for linha in ranking]
    ranking = sorted(ranking, key=lambda linha: int(linha[1]), reverse=True)
    for i, linha in enumerate(ranking):
      print(f"{i + 1} - {linha[0]}: {linha[1]} pontos")

while True:
  titulo('Batalha Naval')
  print('1 - Jogar')
  print('2 - Mostrar ranking')
  print('0 - sair')

  opcao = input('Informe a opcao desejada: ')

  if opcao == '1':
    jogar()
  elif opcao == '2':
    ranking()
  elif opcao == '0':
     break
  else:
     print('Opcao invalida')