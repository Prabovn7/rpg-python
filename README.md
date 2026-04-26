# RPG Python 🎲⚔️

Um jogo de RPG de terminal em Python com **interface colorida e interativa**, desenvolvido para praticar os pilares da **Programação Orientada a Objetos (POO)** com foco em abstração, herança, encapsulamento e polimorfismo.

## ✨ Demonstração

```
╭────────────────────────────────────────╮
│  ⚔️  BEM-VINDO AO COMBATE RPG!  ⚔️   │
╰────────────────────────────────────────╯

╭────────────────────────────────────────╮
│     CRIAÇÃO DO PERSONAGEM 1            │
╰────────────────────────────────────────╯

Escolha sua classe:
  [1] Guerreiro (vida padrão: 1000)
  [2] Mago      (vida padrão: 1000)
Digite 1 ou 2: 1
Digite o nome do Guerreiro: Kratos
Digite a vida do personagem [1000]:

╭────────────────────────────────────────╮
│      🛡️ Guerreiro(nome='Kratos', ...   │
│      🔮 Mago(nome='Merlim', ...)       │
╰────────────────────────────────────────╯

⚔️  O COMBATE COMEÇOU!  ⚔️

╭────────────────────────────────────────╮
│              TURNO 1                   │
╰────────────────────────────────────────╯

╭────────────────────────────────────────╮
│  ⚔️  STATUS DO COMBATE  ⚔️             │
│  Kratos   ████████████████ 1000/1000   │
│  Merlim   ████████████████ 1000/1000   │
╰────────────────────────────────────────╯

⏳ Merlim está preparando o ataque...

⚔️  Merlim usou 'Descarga Elétrica' contra Kratos
   🎲 Dado: 17 | Dano: 621 | Vida de Kratos: 1000 → 379

💖 Kratos se curou! +4 HP | Vida: 379 → 383

╭────────────────────────────────────────╮
│              TURNO 2                   │
╰────────────────────────────────────────╯
...

╭────────────────────────────────────────╮
│  🏆  Merlim VENCEU O COMBATE!  🏆      │
╰────────────────────────────────────────╯
```

## 📋 Sobre o Projeto

Este projeto implementa um sistema de combate RPG interativo onde você cria seus personagens e os coloca para batalhar em turnos. A interface é construída com a biblioteca **Rich**, proporcionando uma experiência visual imersiva no terminal com cores, painéis, barras de progresso e animações.

O sistema inclui:
- **Interface colorida com Rich**: painéis de ~60 colunas, barras de vida, tabelas e texto estilizado
- **Criação interativa de personagens**: escolha nome, vida e classe via terminal
- **Sistema de batalha por turnos**: ataques, curas e vitória automática
- **Mecânica de ataque** baseada em dados (D20), com críticos, falhas críticas e faixas de dano variáveis
- **Mecânica de cura** baseada em dados, com recuperação de vida proporcional ao resultado
- **Pausas dramáticas**: `sleep` entre ações para criar suspense
- **Validações de estado** que impedem ações de personagens mortos ou com vida cheia

## 🏗️ Estrutura do Projeto

```
rpg-python/
├── README.md
├── LICENSE
├── .gitignore
└── projetopy/
    ├── __init__.py
    ├── __main__.py              # Entrada principal — interatividade via input
    └── jogo/
        ├── __init__.py
        ├── ficha.py             # Classe base Personagem (ABC)
        ├── batalha.py           # Classe Batalha — gerencia turnos e fluxo
        ├── interface.py         # Interface visual Rich (~60 col)
        └── personagens/
            ├── __init__.py
            ├── guerreiro.py     # Classe Guerreiro
            └── mago.py          # Classe Mago
```

## 🚀 Como Executar

### Requisitos
- Python 3.10+
- [Rich](https://github.com/Textualize/rich) (`pip install rich`)

### Instalação e Execução

```bash
# Clonar o repositório
git clone https://github.com/usuario/rpg-python.git
cd rpg-python

# Instalar dependências
pip install rich

# Executar o jogo
python -m projetopy
```

## 🎮 Como Jogar

1. **Criar Personagem 1**: escolha entre Guerreiro ou Mago, digite o nome e confirme a vida (padrão: 1000)
2. **Criar Personagem 2**: mesmo processo para o segundo combatente
3. **Pressione Enter** para iniciar o combate
4. **Acompanhe os turnos**: cada personagem ataca e cura automaticamente com pausas dramáticas
5. **Vitória**: o último personagem vivo vence o combate!

## 🎯 Funcionalidades

### Personagens
- **Guerreiro**: Especialista em combate corpo a corpo com alta resistência (vida padrão: 1000)
- **Mago**: Mestre das artes arcanas com golpes elementais (vida padrão: 1000)

### Interface Visual (Rich)
- **Painéis estilizados** (~60 colunas) para boas-vindas, turnos e resultados
- **Barras de vida** coloridas que atualizam a cada turno (bar_width=25)
- **Tabela de status final** com vencedor e dados dos personagens
- **Cores dinâmicas**: dano alto em vermelho, cura em verde, críticos em amarelo
- **Animações de preparação**: mensagens de suspense antes de ataques e curas

### Sistema de Combate
- **Ataque baseado em D20**: Resultados de 1 a 20 determinam a eficácia do golpe
  - **1**: Falha crítica (0 de dano)
  - **2-10**: Dano baixo (até 30% da força)
  - **11-14**: Dano médio (30-50% da força)
  - **15-19**: Dano alto (50-90% da força)
  - **20**: Crítico (100% da força, multiplicado por 2)

### Sistema de Cura
- **Cura baseada em D20**: Resultados de 1 a 20 determinam a quantidade recuperada
  - **1-10**: Cura baixa (0-30 HP)
  - **11-14**: Cura média (30-60 HP)
  - **15-19**: Cura alta (60-99 HP)
  - **20**: Cura máxima (100 HP)

### Validações
- Nome do personagem não pode ser vazio
- Vida inicial deve ser maior que 0
- Personagens mortos não podem atacar nem curar
- Não é possível curar além da vida máxima
- Não é possível curar com a vida cheia

## 💡 Conceitos de POO Aplicados

| Pilar | Aplicação no Projeto |
|-------|----------------------|
| **Abstração** | Classe `Personagem` (ABC) define a estrutura e comportamentos comuns |
| **Herança** | `Guerreiro` e `Mago` herdam de `Personagem`, reutilizando lógica de ataque, cura e dano |
| **Encapsulamento** | Atributos tipados, validações internas e métodos protegidos (`_calcular_dano`, `_aplicar_cura`) |
| **Polimorfismo** | Cada classe define sua própria lista de `golpes`; a lógica de cura é compartilhada mas extensível |

## 📝 Exemplo de Uso Programático

```python
from projetopy.jogo import Guerreiro, Mago, Batalha

# Criar personagens
guerreiro = Guerreiro(nome="Kratos", vida=2000)
mago = Mago(nome="Merlim", vida=2000)

# Iniciar batalha
batalha = Batalha(guerreiro, mago)
batalha.iniciar()  # Interface Rich automática!
```

Ou use os métodos individualmente:

```python
# Executar ações manualmente
resultado_ataque = guerreiro.atacar(alvo=mago, forca=1000)
print(resultado_ataque)
# {
#   'tipo': 'ataque',
#   'dado': 15,
#   'atacante': 'Kratos',
#   'alvo': 'Merlim',
#   'golpe': 'Chute Giratório',
#   'forca': 1000,
#   'dano': 720,
#   'critico': False,
#   'falha': False,
#   'vida_antes': 2000,
#   'vida_depois': 1280
# }

resultado_cura = mago.curar()
print(resultado_cura)
# {
#   'tipo': 'cura',
#   'sucesso': True,
#   'personagem': 'Merlim',
#   'cura': 45,
#   'vida_antes': 1280,
#   'vida_depois': 1325
# }
```

## 🛠️ Tecnologias e Boas Práticas

- **[Rich](https://github.com/Textualize/rich)**: Biblioteca para interfaces de terminal modernas e coloridas
- **Painéis responsivos**: Largura fixa de ~60 colunas para melhor visualização em terminais padrão
- **Type Hints**: Anotações de tipo em todos os métodos e parâmetros
- **Docstrings**: Documentação completa de classes e métodos
- **Constantes**: Valores mágicos extraídos para constantes de classe nomeadas
- **Validações**: Verificações de entrada e estado para prevenir erros em runtime
- **Retornos Padronizados**: Dicionários estruturados para todas as ações, facilitando testes e integração

## 📚 Sobre este Projeto

Este é o **Desafio 27** do curso de **Programação Orientada a Objetos em Python** do canal [Curso em Vídeo](https://www.cursoemvideo.com), ministrado pelo professor [Gustavo Guanabara](https://github.com/gustavoguanabara).

O código foi refatorado para aplicar boas práticas de desenvolvimento, incluindo:
- Interface visual interativa com Rich (painéis de ~60 colunas)
- Sistema de batalha completo com turnos
- Eliminação de código duplicado
- Padronização de retornos entre classes
- Adição de validações e tratamento de erros
- Melhoria na organização e documentação do código

## 🖼️ Interface no Terminal

O jogo utiliza:
- **Painéis** (`Panel`, `width=60`) para organizar seções com tamanho adequado
- **Barras de progresso** (`Progress`, `bar_width=25`) para vida dos personagens
- **Tabelas** (`Table`, `width=60`) para status final
- **Texto estilizado** (`Text`) para títulos e destaques
- **Cores dinâmicas**: vermelho (perigo), verde (cura), amarelo (crítico), cyan (info)

