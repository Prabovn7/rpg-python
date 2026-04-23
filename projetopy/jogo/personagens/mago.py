from ..ficha import Personagem



class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de fogo", "Descarga Elétrica",
                       "Lançamento de Rocha", "Prisão aquática", "Explosão elemental"]

    def curar(self):
        if self.vida >= self.vida_maxima:
            print(f"{self.nome} já está com a vida cheia!")
            return 0

        cura = self.calcular_cura()
        cura_real = min(cura, self.vida_maxima - self.vida)

        self.vida += cura_real

        print(
            f"{self.nome} fez uma magia de cura e recuperou {cura_real} pontos de vida!")

        return cura_real
