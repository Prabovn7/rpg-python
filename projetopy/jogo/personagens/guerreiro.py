from ..ficha import Personagem
from rich import print


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco direto", "Chute",
                       "Rasteira", "Soco cruzado", "Chute Giratório"]

    def curar(self):
        if self.vida >= self.vida_maxima:
            print(f"{self.nome} já está com a vida cheia!")
            return 0

        cura = self.calcular_cura()
        cura_real = min(cura, self.vida_maxima - self.vida)

        self.vida += cura_real

        print(
            f"[cyan]{self.nome}[/] enrolou uma atadura nos ferimentos e recuperou [green]{cura_real} pontos de vida[/]!")

        return cura_real
