from abc import ABC, abstractmethod
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
        dado = randint(1, 20)
        golpe = choice(self.golpes) if self.golpes else "ataque básico"

        dano, critico, falha = self._calcular_dano(forca, dado)

        vida_antes = alvo.vida

        if not falha:
            dano_real = alvo.receber_dano(dano)
        else:
            dano_real = 0

        return {
            "tipo": "ataque",
            "dado": dado,
            "atacante": self.nome,
            "alvo": alvo.nome,
            "golpe": golpe,
            "forca": forca,
            "dano": dano_real,
            "critico": critico,
            "falha": falha,
            "vida_antes": vida_antes,
            "vida_depois": alvo.vida
        }

    def _calcular_dano(self, forca, dado):
        critico = dado == 20
        falha = dado == 1

        if falha:
            return 0, critico, falha

        if dado <= 10:
            dano = randint(1, int(forca * 0.3))
        elif dado <= 14:
            dano = randint(int(forca * 0.3), int(forca * 0.5))
        elif dado <= 19:
            dano = randint(int(forca * 0.5), int(forca * 0.9))
        else:  # dado == 20
            dano = forca

        if critico:
            dano *= 2

        return dano, critico, falha

    def receber_dano(self, dano):
        dano_real = max(0, dano)
        self.vida = max(0, self.vida - dano_real)
        return dano_real

    def calcular_cura(self):
        dado = randint(1, 20)

        if dado <= 10:
            return randint(0, 30)
        elif dado <= 14:
            return randint(30, 60)
        elif dado <= 19:
            return randint(60, 99)
        else:
            return 100

    def esta_vivo(self):
        return self.vida > 0
