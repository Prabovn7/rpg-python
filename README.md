# RPG Python 🎲⚔️

Um jogo de RPG em Python desenvolvido para praticar os pilares da **Programação Orientada a Objetos (POO)**, com foco em abstração, herança, encapsulamento e polimorfismo.

## 📋 Sobre o Projeto

Este projeto implementa um sistema de combate RPG simples onde diferentes tipos de personagens (Guerreiro, Mago) possuem habilidades, atributos e golpes únicos. O código demonstra como usar POO para criar uma hierarquia de classes extensível, reutilizável e bem documentada.

O sistema inclui:
- **Mecânica de ataque** baseada em dados (D20), com críticos, falhas críticas e faixas de dano variáveis
- **Mecânica de cura** baseada em dados, com recuperação de vida proporcional ao resultado
- **Validações de estado** que impedem ações de personagens mortos ou com vida cheia
- **Retorno estruturado** de todas as ações em dicionários tipados, facilitando integração com interfaces (CLI, GUI, API)

## 🏗️ Estrutura do Projeto

```
rpg-python/
├── README.md
├── LICENSE
├── .gitignore
└── projetopy/
    ├── __init__.py
    ├── __main__.py              # Entrada principal do jogo
    └── jogo/
        ├── __init__.py
        ├── ficha.py             # Classe base Personagem (ABC)
        └── personagens/
            ├── __init__.py
            ├── guerreiro.py     # Classe Guerreiro
            └── mago.py          # Classe Mago
```

## 🚀 Como Executar

### Requisitos
- Python 3.10+

### Instalação e Execução

```bash
# Clonar o repositório
git clone https://github.com/usuario/rpg-python.git
cd rpg-python

# Executar o jogo
python -m projetopy
```

## 🎯 Funcionalidades

### Personagens
- **Guerreiro**: Especialista em combate corpo a corpo com alta resistência (vida padrão: 120)
- **Mago**: Mestre das artes arcanas com golpes elementais (vida padrão: 80)

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

## 📝 Exemplo de Uso

```python
from projetopy.jogo import Guerreiro, Mago

# Criar personagens
guerreiro = Guerreiro(nome="Kratos", vida=2000)
mago = Mago(nome="Merlim", vida=2000)

# Executar ações
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

- **Type Hints**: Anotações de tipo em todos os métodos e parâmetros
- **Docstrings**: Documentação completa de classes e métodos
- **Constantes**: Valores mágicos extraídos para constantes de classe nomeadas
- **Validações**: Verificações de entrada e estado para prevenir erros em runtime
- **Retornos Padronizados**: Dicionários estruturados para todas as ações, facilitando testes e integração

## 📚 Sobre este Projeto

Este é o **Desafio 27** do curso de **Programação Orientada a Objetos em Python** do canal [Curso em Vídeo](https://www.cursoemvideo.com), ministrado pelo professor [Gustavo Guanabara](https://github.com/gustavoguanabara).

O código foi refatorado para aplicar boas práticas de desenvolvimento, incluindo:
- Eliminação de código duplicado
- Padronização de retornos entre classes
- Adição de validações e tratamento de erros
- Melhoria na organização e documentação do código
