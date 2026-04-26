import time

from .ficha import Personagem
from .interface import (
    console,
    titulo_turno,
    animacao_preparacao,
    exibir_ataque,
    exibir_cura,
    morte_personagem,
    tela_vitoria,
    painel_combate,
)


class Batalha:
    """Gerencia o fluxo de uma batalha entre dois personagens."""

    def __init__(self, jogador1: Personagem, jogador2: Personagem) -> None:
        """Inicializa a batalha com dois combatentes.

        Args:
            jogador1: Primeiro personagem.
            jogador2: Segundo personagem.
        """
        self.jogadores = [jogador1, jogador2]
        self.turno = 1

    def iniciar(self) -> None:
        """Executa a batalha completa até haver um vencedor."""
        console.print()
        console.print(
            "[bold red]⚔️  O COMBATE COMEÇOU!  ⚔️[/bold red]",
            justify="center",
        )
        console.print()
        time.sleep(1.0)

        while self.jogadores[0].esta_vivo() and self.jogadores[1].esta_vivo():
            self._executar_turno()
            self.turno += 1

        self._exibir_resultado_final()

    def _executar_turno(self) -> None:
        """Executa um único turno de batalha."""
        atacante = self.jogadores[self.turno % 2]
        defensor = self.jogadores[(self.turno + 1) % 2]

        titulo_turno(self.turno)

        # Mostra status atual antes da ação
        painel_combate(self.jogadores[0], self.jogadores[1])
        time.sleep(0.5)

        # Ataque
        animacao_preparacao(atacante.nome, "preparando o ataque", "yellow")
        time.sleep(0.5)

        resultado = atacante.atacar(defensor, 1000)
        exibir_ataque(resultado)

        if not defensor.esta_vivo():
            morte_personagem(defensor.nome)
            return

        # Cura do defensor
        time.sleep(0.5)
        animacao_preparacao(defensor.nome, "se concentrando para curar", "green")
        time.sleep(0.5)

        resultado_cura = defensor.curar()
        exibir_cura(resultado_cura)

        time.sleep(0.8)

    def _exibir_resultado_final(self) -> None:
        """Exibe o vencedor e o status final dos personagens."""
        vencedor = (
            self.jogadores[0]
            if self.jogadores[0].esta_vivo()
            else self.jogadores[1]
        )

        tela_vitoria(vencedor, self.jogadores[0], self.jogadores[1])
