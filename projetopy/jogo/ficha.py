from abc import ABC, abstractmethod
from random import randint, choice


class Personagem(ABC):
    """Classe base abstrata para personagens de RPG.

    Define atributos comuns (nome, vida, golpes) e comportamentos
    de ataque, cura e recebimento de dano.
    """

    # Constantes do sistema de dados
    DADO_MIN: int = 1
    DADO_MAX: int = 20
    CRITICO: int = 20
    FALHA: int = 1

    # Faixas de dano por resultado do dado
    DANO_FAIXA_BAIXA_MAX: int = 10
    DANO_FAIXA_MEDIA_MAX: int = 14
    DANO_FAIXA_ALTA_MAX: int = 19

    # Multiplicadores de dano
    DANO_MULT_BAIXO: float = 0.3
    DANO_MULT_MEDIO: float = 0.5
    DANO_MULT_ALTO: float = 0.9

    # Faixas de cura por resultado do dado
    CURA_FAIXA_BAIXA_MAX: int = 10
    CURA_FAIXA_MEDIA_MAX: int = 14
    CURA_FAIXA_ALTA_MAX: int = 19

    # Limites de cura
    CURA_MIN: int = 0
    CURA_BAIXA_MAX: int = 30
    CURA_MEDIA_MAX: int = 60
    CURA_ALTA_MAX: int = 99
    CURA_MAXIMA: int = 100

    def __init__(self, nome: str, vida: int) -> None:
        """Inicializa um personagem.

        Args:
            nome: Nome do personagem.
            vida: Pontos de vida máximos (deve ser maior que 0).

        Raises:
            ValueError: Se o nome for vazio ou a vida for menor ou igual a 0.
        """
        if not nome or not nome.strip():
            raise ValueError("O nome do personagem não pode ser vazio.")
        if vida <= 0:
            raise ValueError("A vida inicial deve ser maior que 0.")

        self.nome: str = nome
        self.vida: int = vida
        self.vida_maxima: int = vida
        self.golpes: list[str] = []

    def __repr__(self) -> str:
        """Retorna uma representação legível do personagem para debug."""
        return (
            f"{self.__class__.__name__}("
            f"nome={self.nome!r}, vida={self.vida}/{self.vida_maxima})"
        )

    def curar(self) -> dict:
        """Executa a ação de cura do personagem.

        Returns:
            Dicionário com os detalhes da cura realizada.
        """
        return self._aplicar_cura()

    def _aplicar_cura(self) -> dict:
        """Lógica concreta de cura compartilhada entre as subclasses.

        Returns:
            Dicionário com os detalhes da cura realizada.
        """
        if self.vida >= self.vida_maxima:
            return {
                "tipo": "cura",
                "sucesso": False,
                "motivo": "vida_cheia",
                "personagem": self.nome,
                "cura": 0,
                "vida_antes": self.vida,
                "vida_depois": self.vida,
            }

        if not self.esta_vivo():
            return {
                "tipo": "cura",
                "sucesso": False,
                "motivo": "personagem_morto",
                "personagem": self.nome,
                "cura": 0,
                "vida_antes": self.vida,
                "vida_depois": self.vida,
            }

        cura = self.calcular_cura()
        vida_antes = self.vida
        cura_real = min(cura, self.vida_maxima - self.vida)
        self.vida += cura_real

        return {
            "tipo": "cura",
            "sucesso": True,
            "personagem": self.nome,
            "cura": cura_real,
            "vida_antes": vida_antes,
            "vida_depois": self.vida,
        }

    def atacar(self, alvo: "Personagem", forca: int) -> dict:
        """Executa um ataque contra outro personagem.

        Args:
            alvo: Personagem que será atacado.
            forca: Força base do ataque (deve ser >= 0).

        Returns:
            Dicionário com os detalhes do ataque realizado.

        Raises:
            ValueError: Se a força for negativa ou se algum dos personagens estiver morto.
        """
        if forca < 0:
            raise ValueError("A força do ataque não pode ser negativa.")
        if not self.esta_vivo():
            raise ValueError(f"{self.nome} está morto e não pode atacar.")
        if not alvo.esta_vivo():
            raise ValueError(f"{alvo.nome} já está morto e não pode ser atacado.")

        dado = randint(self.DADO_MIN, self.DADO_MAX)
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
            "vida_depois": alvo.vida,
        }

    def _calcular_dano(self, forca: int, dado: int) -> tuple[int, bool, bool]:
        """Calcula o dano com base na força e no resultado do dado.

        Args:
            forca: Força base do ataque.
            dado: Resultado do lançamento do dado (1 a 20).

        Returns:
            Tupla contendo (dano, critico, falha).
        """
        critico = dado == self.CRITICO
        falha = dado == self.FALHA

        if falha:
            return 0, critico, falha

        if dado <= self.DANO_FAIXA_BAIXA_MAX:
            dano = randint(1, int(forca * self.DANO_MULT_BAIXO))
        elif dado <= self.DANO_FAIXA_MEDIA_MAX:
            dano = randint(int(forca * self.DANO_MULT_BAIXO), int(forca * self.DANO_MULT_MEDIO))
        elif dado <= self.DANO_FAIXA_ALTA_MAX:
            dano = randint(int(forca * self.DANO_MULT_MEDIO), int(forca * self.DANO_MULT_ALTO))
        else:  # dado == 20 (crítico)
            dano = forca

        if critico:
            dano *= 2

        return dano, critico, falha

    def receber_dano(self, dano: int) -> int:
        """Aplica dano ao personagem, garantindo que a vida não fique negativa.

        Args:
            dano: Quantidade de dano a ser aplicada.

        Returns:
            Dano real aplicado.
        """
        dano_real = max(0, dano)
        self.vida = max(0, self.vida - dano_real)
        return dano_real

    def calcular_cura(self) -> int:
        """Calcula o valor da cura com base em um lançamento de dado.

        Returns:
            Quantidade de pontos de vida recuperados.
        """
        dado = randint(self.DADO_MIN, self.DADO_MAX)

        if dado <= self.CURA_FAIXA_BAIXA_MAX:
            return randint(self.CURA_MIN, self.CURA_BAIXA_MAX)
        elif dado <= self.CURA_FAIXA_MEDIA_MAX:
            return randint(self.CURA_BAIXA_MAX, self.CURA_MEDIA_MAX)
        elif dado <= self.CURA_FAIXA_ALTA_MAX:
            return randint(self.CURA_MEDIA_MAX, self.CURA_ALTA_MAX)
        else:
            return self.CURA_MAXIMA

    def esta_vivo(self) -> bool:
        """Verifica se o personagem ainda está vivo.

        Returns:
            True se a vida for maior que 0, False caso contrário.
        """
        return self.vida > 0

