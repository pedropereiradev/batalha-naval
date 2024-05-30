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

tabuleiro = [
    [" " for i in range(15)] for j in range(15)
]

# def posicionar_embarcacoes():
#   for embarcacao in embarcacoes:
#     for i in range(embarcacao["quantidade"]):
#       print(f"Posicione o {embarcacao['nome']} {i + 1}/{embarcacao['quantidade']}")
#       while True:
#         x = int(input("X: "))
#         y = int(input("Y: "))
#         direcao = input("Direção (h/v): ")
# 
#         if direcao == "h":
#           if x + embarcacao["tamanho"] <= len(tabuleiro) and all(tabuleiro[y][x + j] == " " for j in range(embarcacao["tamanho"])):
#             for j in range(embarcacao["tamanho"]):
#               tabuleiro[y][x + j] = embarcacao["nome"][0]
#             break
#         else:
#           if y + embarcacao["tamanho"] <= len(tabuleiro) and all(tabuleiro[y + j][x] == " " for j in range(embarcacao["tamanho"])):
#             for j in range(embarcacao["tamanho"]):
#               tabuleiro[y + j][x] = embarcacao["nome"][0]
#             break

def posicionar_embarcacoes_random():
  for embarcacao in embarcacoes:
    for i in range(embarcacao["quantidade"]):
      print(f"Posicione o {embarcacao['nome']} {i + 1}/{embarcacao['quantidade']}")
      while True:
        x = random.randint(0, 14)
        y = random.randint(0, 14)
        direcao = random.choice(["h", "v"])

        if direcao == "h":
          if x + embarcacao["tamanho"] <= len(tabuleiro) and all(tabuleiro[y][x + j] == " " for j in range(embarcacao["tamanho"])):
            for j in range(embarcacao["tamanho"]):
              tabuleiro[y][x + j] = embarcacao["nome"][0]
            break
        else:
          if y + embarcacao["tamanho"] <= len(tabuleiro) and all(tabuleiro[y + j][x] == " " for j in range(embarcacao["tamanho"])):
            for j in range(embarcacao["tamanho"]):
              tabuleiro[y + j][x] = embarcacao["nome"][0]
            break

def imprimir_tabuleiro():
    print("  01 02 03 04 05 06 07 08 09 10 11 12 13 14")
    for i in range(15):
        if i < 10:
          print(f"0{i} {' '.join(tabuleiro[i])}")
        else:
          print(f"{i} {' '.join(tabuleiro[i])}")

posicionar_embarcacoes_random()
imprimir_tabuleiro()
