from abc import ABC, abstractmethod
from rich import print
from random import randint, choice


class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.vida_maxima = vida
        self.golpes = []

    @abstractmethod
    def curar(self):
        pass

    def atacar(self, alvo, forca):
        dado = (randint(1, 20))
        golpe = choice(self.golpes)

        if dado <= 10:  # dano minimo
            dano = randint(1, int(forca*0.3))

        elif dado < 15:  # dano medio
            dano = randint(int(forca*0.3), int(forca*0.5))

        elif dado <= 19:  # dano alto
            dano = randint(int(forca*0.5), int(forca*0.9))

        elif dado == 20:  # dano maximo
            dano = forca
        vida_antes = alvo.vida
        alvo.receber_dano(dano)

        print(f"[green]{self.nome}[/]([cyan]{self.vida}[/]) atacou [red]{alvo.nome}[/]([cyan]{vida_antes}[/]) com um [blue]{golpe}[/] de força {forca}")
        print(f"[red]{alvo.nome}[/] recebeu [red]dano de {dano}[/]!")

    def receber_dano(self, dano):
        self.vida = max(0, self.vida - dano)

    def calcular_cura(self):
        dado = randint(1, 20)
        if dado <= 10:
            cura = randint(0, 30)
        elif dado < 15:
            cura = randint(30, 60)
        elif dado <= 19:
            cura = randint(60, 99)
        elif dado == 20:
            cura = 100

        return cura
