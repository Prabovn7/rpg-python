# RPG Python 🎮

Um jogo de RPG em Python desenvolvido para praticar os pilares da **Programação Orientada a Objetos (POO)**, com foco em abstração, herança.

## 📋 Sobre o Projeto

Este projeto implementa um sistema de jogo RPG simples onde diferentes tipos de personagens (Guerreiro, Mago) possuem habilidades e atributos únicos. O código demonstra como usar abstração e herança para criar uma hierarquia de classes extensível.

## 🏗️ Estrutura do Projeto

```
rpg-python/
├── README.md
├── LICENSE
└── projetopy/
    ├── __main__.py           # Entrada principal do jogo
    ├── jogo/
    │   ├── __init__.py
    │   ├── ficha.py          # Classe base Ficha
    │   └── personagens/
    │       ├── __init__.py
    │       ├── guerreiro.py  # Classe Guerreiro
    │       └── mago.py       # Classe Mago
```

## 🚀 Como Executar

### Requisitos
- Python 3.7+

### Instalação e Execução

```bash
# Clonar o repositório
git clone https://github.com/usuario/rpg-python.git
cd rpg-python

# Executar o jogo
python -m projetopy
```

## 🎯 Funcionalidades

- **Personagens**: Sistema de criação de personagens com diferentes classes
- **Guerreiro**: Focado em força e defesa
- **Mago**: Focado em magia e inteligência
- **Herança**: Todos os personagens herdam da classe base `Ficha`
- **Abstração**: Implementação de comportamentos polimórficos

## 💡 Conceitos de POO Aplicados

- ✅ **Abstração**: Classe base `Ficha` define a estrutura comum
- ✅ **Herança**: Guerreiro e Mago herdam de Ficha
- ✅ **Encapsulamento**: Atributos privados e métodos públicos
- ✅ **Polimorfismo**: Comportamentos específicos por classe

## 📝 Exemplo de Uso

```python
from projetopy.jogo.personagens.guerreiro import Guerreiro
from projetopy.jogo.personagens.mago import Mago

# Criar personagens
guerreiro = Guerreiro(nome="Aragorn")
mago = Mago(nome="Gandalf")

# Usar habilidades
guerreiro.atacar()
mago.lancar_magia()
```

## � Sobre este Projeto

Este é o **Desafio 27** do curso de **Programação Orientada a Objetos em Python** do canal [Curso em Vídeo](https://www.cursoemvideo.com), ministrado pelo professor [Gustavo Guanabara](https://github.com/gustavoguanabara).
