from ..ficha import Personagem


class Guerreiro(Personagem):
    """Representa um personagem guerreiro no RPG.

    Herda de Personagem e define golpes corpo a corpo típicos de um guerreiro.
    """

    def __init__(self, nome: str, vida: int = 1000) -> None:
        """Inicializa um Guerreiro.

        Args:
            nome: Nome do guerreiro.
            vida: Pontos de vida máximos. Padrão é 1000.
        """
        super().__init__(nome, vida)

        self.golpes: list[str] = [
            "Soco direto",
            "Chute",
            "Rasteira",
            "Soco cruzado",
            "Chute Giratório",
        ]

