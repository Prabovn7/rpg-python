"""Interface visual do jogo usando a biblioteca Rich."""

import time

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn
from rich.align import Align
from rich.text import Text
from rich.layout import Layout

from .ficha import Personagem


console = Console()


def tela_boas_vindas() -> None:
    """Exibe a tela de boas-vindas do jogo."""
    console.print()
    console.print(
        Panel.fit(
            Text("⚔️  BEM-VINDO AO COMBATE RPG!  ⚔️", style="bold yellow", justify="center"),
            border_style="bright_blue",
            padding=(1, 4),
        )
    )
    console.print()


def painel_criacao_personagem(numero: int) -> None:
    """Exibe o painel de criação de personagem."""
    console.print()
    console.print(
        Panel.fit(
            f"[bold cyan]CRIAÇÃO DO PERSONAGEM {numero}[/bold cyan]",
            border_style="cyan",
            padding=(0, 2),
        )
    )


def menu_classes() -> None:
    """Exibe o menu de seleção de classes."""
    console.print("\n[bold]Escolha sua classe:[/bold]")
    console.print("  [green][1][/green] Guerreiro (vida padrão: 1000)")
    console.print("  [magenta][2][/magenta] Mago      (vida padrão: 1000)")


def input_estilizado(prompt: str, style: str = "bold white") -> str:
    """Exibe um input estilizado e retorna a resposta do usuário."""
    console.print(f"[{style}]{prompt}[/{style}]", end="")
    return input()


def mensagem_erro(texto: str) -> None:
    """Exibe uma mensagem de erro em vermelho."""
    console.print(f"[bold red]❌ {texto}[/bold red]")


def painel_personagens_criados(j1: Personagem, j2: Personagem) -> None:
    """Exibe um painel com os personagens criados."""
    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_row("🛡️", str(j1), style="green")
    table.add_row("🔮", str(j2), style="magenta")

    console.print()
    console.print(
        Panel(
            Align.center(table),
            title="[bold yellow]PERSONAGENS CRIADOS[/bold yellow]",
            border_style="bright_blue",
        )
    )
    console.print()


def barra_vida(personagem: Personagem, cor: str) -> Progress:
    """Cria uma barra de progresso representando a vida do personagem."""
    progress = Progress(
        TextColumn(f"[bold {cor}]{personagem.nome:<15}[/bold {cor}]"),
        BarColumn(bar_width=30, complete_style=cor, finished_style="green"),
        TextColumn("[bold]{task.completed}/{task.total} HP[/bold]"),
        expand=False,
    )
    progress.add_task("", total=personagem.vida_maxima, completed=personagem.vida)
    return progress


def painel_combate(j1: Personagem, j2: Personagem) -> None:
    """Exibe o painel de status do combate com barras de vida."""
    cor1 = "green" if isinstance(j1.__class__.__name__, str) and "Guerreiro" in j1.__class__.__name__ else "green"
    cor2 = "magenta" if isinstance(j2.__class__.__name__, str) and "Mago" in j2.__class__.__name__ else "magenta"

    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_row(barra_vida(j1, "green"))
    table.add_row(barra_vida(j2, "magenta"))

    console.print()
    console.print(
        Panel(
            Align.center(table),
            title="[bold red]⚔️  STATUS DO COMBATE  ⚔️[/bold red]",
            border_style="red",
        )
    )


def animacao_preparacao(nome: str, acao: str, cor: str = "yellow") -> None:
    """Exibe uma animação de preparação com cor."""
    console.print(f"\n[{cor}]⏳ {nome} está {acao}...[/{cor}]")
    time.sleep(0.8)


def exibir_ataque(resultado: dict) -> None:
    """Exibe o resultado de um ataque com cores e estilos."""
    if resultado["falha"]:
        console.print(
            f"\n[bold red]💥 {resultado['atacante']} tentou usar "
            f"'{resultado['golpe']}' mas FALHOU CRITICAMENTE![/bold red]"
        )
        return

    critico = " [bold yellow](CRÍTICO! 🌟)[/bold yellow]" if resultado["critico"] else ""
    console.print(
        f"\n[bold cyan]⚔️  {resultado['atacante']}[/bold cyan] usou "
        f"[bold white]'{resultado['golpe']}'[/bold white] contra "
        f"[bold red]{resultado['alvo']}[/bold red]{critico}"
    )
    time.sleep(0.3)

    dano_cor = "red" if resultado["dano"] > 500 else "yellow" if resultado["dano"] > 200 else "green"
    console.print(
        f"   🎲 Dado: [bold]{resultado['dado']}[/bold] | "
        f"Dano: [bold {dano_cor}]{resultado['dano']}[/bold {dano_cor}] | "
        f"Vida de [bold]{resultado['alvo']}[/bold]: "
        f"[green]{resultado['vida_antes']}[/green] → "
        f"[red]{resultado['vida_depois']}[/red]"
    )


def exibir_cura(resultado: dict) -> None:
    """Exibe o resultado de uma cura com cores."""
    if not resultado["sucesso"]:
        if resultado.get("motivo") == "vida_cheia":
            console.print(
                f"\n[bold yellow]❌ {resultado['personagem']} já está com a vida cheia![/bold yellow]"
            )
        elif resultado.get("motivo") == "personagem_morto":
            console.print(
                f"\n[bold red]💀 {resultado['personagem']} está morto e não pode curar![/bold red]"
            )
        return

    console.print(
        f"\n[bold green]💖 {resultado['personagem']} se curou! [/bold green]"
        f"[bold white]+{resultado['cura']} HP[/bold white] | "
        f"Vida: [red]{resultado['vida_antes']}[/red] → "
        f"[green]{resultado['vida_depois']}[/green]"
    )


def titulo_turno(numero: int) -> None:
    """Exibe o título do turno com destaque."""
    console.print()
    console.print(
        Panel.fit(
            f"[bold yellow]TURNO {numero}[/bold yellow]",
            border_style="yellow",
            padding=(0, 4),
        )
    )


def morte_personagem(nome: str) -> None:
    """Exibe a mensagem de morte com efeito dramático."""
    time.sleep(0.5)
    console.print(f"\n[bold red on_black]💀 {nome} foi derrotado![/bold red on_black]")


def tela_vitoria(vencedor: Personagem, j1: Personagem, j2: Personagem) -> None:
    """Exibe a tela de vitória com celebração."""
    time.sleep(0.8)
    console.print()
    console.print(
        Panel.fit(
            Text(f"🏆  {vencedor.nome} VENCEU O COMBATE!  🏆", style="bold yellow", justify="center"),
            border_style="green",
            padding=(1, 4),
        )
    )

    time.sleep(0.5)
    table = Table(title="📊 STATUS FINAL", title_style="bold cyan", border_style="blue")
    table.add_column("Personagem", style="bold")
    table.add_column("Vida", justify="center")
    table.add_column("Status", justify="center")

    for jogador in [j1, j2]:
        status = "[green]VIVO[/green]" if jogador.esta_vivo() else "[red]DERROTADO[/red]"
        table.add_row(
            f"{jogador.__class__.__name__} {jogador.nome}",
            f"{jogador.vida}/{jogador.vida_maxima}",
            status,
        )

    console.print(table)
    console.print()


def aguardar_enter() -> None:
    """Pausa o jogo até o usuário pressionar Enter."""
    console.print("\n[dim]Pressione Enter para continuar...[/dim]", end="")
    input()
