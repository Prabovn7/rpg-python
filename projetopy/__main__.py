from projetopy.jogo import Personagem, Mago, Guerreiro


def main():
    j1 = Guerreiro("Kratos", 2000)
    j2 = Mago("Merlim", 2000)

    print(j1.atacar(j2, 1000))
    print(j2.curar())
    print(j2.atacar(j1, 1000))
    print(j1.curar())
    print(j1.atacar(j2, 1000))


if __name__ == "__main__":
    main()

