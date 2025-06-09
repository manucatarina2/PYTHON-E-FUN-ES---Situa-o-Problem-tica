import random
import time

def criar_personagem(tipo):
    if tipo == "Mago":
        return {"nome": "Mago", "vida": 80, "ataque": 25, "defesa": 10, "forca": 20}
    elif tipo == "Arqueiro":
        return {"nome": "Arqueiro", "vida": 90, "ataque": 20, "defesa": 15, "forca": 25}
    elif tipo == "Guerreiro":
        return {"nome": "Guerreiro", "vida": 120, "ataque": 15, "defesa": 20, "forca": 30}

def exibir_status(personagem):
    print(f"\n--- {personagem['nome']} ---")
    print(f"Vida: {personagem['vida']}")
    print(f"Ataque: {personagem['ataque']}")
    print(f"Defesa: {personagem['defesa']}")
    print(f"Força: {personagem['forca']}")
    print("---------------------------")

def atacar(atacante, defensor):
    dano = atacante["ataque"] + atacante["forca"] - defensor["defesa"]
    dano = max(dano, 5)  
    defensor["vida"] -= dano
    defensor["vida"] = max(defensor["vida"], 0)
    print(f"{atacante['nome']} atacou {defensor['nome']} causando {dano} de dano!")

classes = ["Mago", "Arqueiro", "Guerreiro"]

print("Escolha seu personagem:")
for i, classe in enumerate(classes, 1):
    print(f"{i}. {classe}")

opcao = int(input("Digite o número da classe: "))
jogador = criar_personagem(classes[opcao - 1])

inimigo_opcoes = classes[:]
inimigo_opcoes.remove(jogador["nome"])
inimigo = criar_personagem(random.choice(inimigo_opcoes))

print("\nVocê escolheu:")
exibir_status(jogador)

print("\nSeu inimigo é:")
exibir_status(inimigo)

print("\n=== BATALHA INICIADA ===")
round = 1
while jogador["vida"] > 0 and inimigo["vida"] > 0:
    print(f"\n--- Round {round} ---")
    atacar(jogador, inimigo)
    if inimigo["vida"] <= 0:
        print(f"\n{inimigo['nome']} foi derrotado! Você venceu!")
        break

    atacar(inimigo, jogador)
    if jogador["vida"] <= 0:
        print(f"\n{jogador['nome']} foi derrotado! Você perdeu!")
        break

    exibir_status(jogador)
    exibir_status(inimigo)
    round += 1
    time.sleep(1) 
