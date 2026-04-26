from ..ficha import Personagem


class Mago(Personagem):
    """Representa um personagem mago no RPG.

    Herda de Personagem e define golpes mágicos elementais típicos de um mago.
    """

    def __init__(self, nome: str, vida: int = 80) -> None:
        """Inicializa um Mago.

        Args:
            nome: Nome do mago.
            vida: Pontos de vida máximos. Padrão é 80.
        """
        super().__init__(nome, vida)

        self.golpes: list[str] = [
            "Bola de fogo",
            "Descarga Elétrica",
            "Lançamento de Rocha",
            "Prisão aquática",
            "Explosão elemental",
        ]

