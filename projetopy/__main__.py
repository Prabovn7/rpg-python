try:
    from projetopy.jogo import Personagem, Mago, Guerreiro, Batalha
    from projetopy.jogo.interface import (
        console,
        tela_boas_vindas,
        painel_criacao_personagem,
        menu_classes,
        input_estilizado,
        mensagem_erro,
        painel_personagens_criados,
        aguardar_enter,
    )
except ModuleNotFoundError:
    from jogo import Personagem, Mago, Guerreiro, Batalha
    from jogo.interface import (
        console,
        tela_boas_vindas,
        painel_criacao_personagem,
        menu_classes,
        input_estilizado,
        mensagem_erro,
        painel_personagens_criados,
        aguardar_enter,
    )


CLASSES_DISPONIVEIS: dict[str, type[Personagem]] = {
    "1": Guerreiro,
    "2": Mago,
}


def escolher_classe(numero_jogador: int) -> type[Personagem]:
    menu_classes()

    while True:
        escolha = input_estilizado("Digite 1 ou 2: ", "bold white")
        if escolha in CLASSES_DISPONIVEIS:
            return CLASSES_DISPONIVEIS[escolha]
        mensagem_erro("Opção inválida! Digite 1 ou 2.")


def escolher_nome(classe: type[Personagem]) -> str:
    while True:
        nome = input_estilizado(f"Digite o nome do {classe.__name__}: ", "bold cyan")
        if nome:
            return nome
        mensagem_erro("O nome não pode ficar vazio!")


def escolher_vida() -> int:
    padrao = 1000
    console.print(f"\n[dim]Vida atual: {padrao} (pressione Enter para manter)[/dim]")

    while True:
        entrada = input_estilizado(
            f"Digite a vida do personagem [{padrao}]: ", "bold white"
        ).strip()
        if not entrada:
            return padrao
        try:
            vida = int(entrada)
            if vida > 0:
                return vida
            mensagem_erro("A vida deve ser maior que 0!")
        except ValueError:
            mensagem_erro("Digite um número inteiro válido!")


def criar_personagem(numero_jogador: int) -> Personagem:
    painel_criacao_personagem(numero_jogador)

    classe = escolher_classe(numero_jogador)
    nome = escolher_nome(classe)
    vida = escolher_vida()

    return classe(nome, vida)


def main() -> None:
    tela_boas_vindas()

    j1 = criar_personagem(1)
    j2 = criar_personagem(2)

    painel_personagens_criados(j1, j2)
    aguardar_enter()

    batalha = Batalha(j1, j2)
    batalha.iniciar()


if __name__ == "__main__":
    main()
