# 🎮 Jogo da Adivinhação

Jogo de adivinhação de números desenvolvido em Python com **Programação Orientada a Objetos (POO)**, utilizando conceitos de abstração, encapsulamento e herança. O jogador tenta adivinhar um número secreto entre 1 e 100, gerenciando sua pontuação conforme a dificuldade escolhida.

---

## Funcionalidades

- Geração aleatória de número secreto (1 a 100)
- Sistema de pontuação dinâmico por dificuldade
- Limite de 10 tentativas por rodada
- Histórico de palpites anteriores (sem repetições)
- Ranking de jogadores ao final da sessão
- Suporte a múltiplos jogadores na mesma sessão

---

## Estrutura do Projeto

```
jogo_adivinhacao/
│
├── jogo.py          # Código principal
└── README.md
```

### Diagrama de Classes

```
Jogo (ABC)
└── JogoAdivinhação
        └── usa → Jogador

Ranking
        └── contém → [Jogador]
```

---

## Classes

### `Jogo` (Classe Abstrata)
Define o contrato base para qualquer jogo. Métodos abstratos:
- `iniciar()` — configura e exibe as regras do jogo
- `jogar()` — executa o loop principal da partida

### `Jogador`
Representa um participante.

| Atributo | Tipo  | Descrição                        |
|----------|-------|----------------------------------|
| `nome`   | `str` | Nome digitado pelo jogador       |
| `pontos` | `int` | Pontuação (começa em 100 pontos) |

### `JogoAdivinhação`
Herda de `Jogo`. Controla toda a lógica da partida.

| Atributo                  | Tipo   | Descrição                              |
|---------------------------|--------|----------------------------------------|
| `_numero_secreto`         | `int`  | Número gerado aleatoriamente           |
| `_tentativas`             | `int`  | Contador de tentativas usadas          |
| `_limite`                 | `int`  | Máximo de 10 tentativas                |
| `dificuldade_penalidade`  | `int`  | Pontos descontados por erro            |
| `_palpites_anteriores`    | `list` | Histórico de palpites para evitar repetições |

### `Ranking`
Gerencia a lista de jogadores e exibe a classificação final ordenada por pontuação.

---

## Dificuldades

| Nível    | Penalidade por erro |
|----------|---------------------|
| Fácil    | -2 pontos           |
| Médio    | -5 pontos           |
| Difícil  | -15 pontos          |

> **Acerto:** +10 pontos independente da dificuldade.

---

## Como Executar

### Pré-requisitos
- Python 3.8 ou superior

### Instalação
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/jogo-adivinhacao.git

# Acesse a pasta
cd jogo-adivinhacao
```

### Execução
```bash
python jogo.py
```

Ou pelo **Google Colab**: acesse o notebook e execute todas as células em ordem.

---

## Como Jogar

1. Digite seu nome quando solicitado
2. Escolha a dificuldade: `facil`, `medio` ou `dificil`
3. Digite palpites entre 1 e 100
4. O jogo informa se o número secreto é **maior** ou **menor**
5. Acerte antes de usar as 10 tentativas para ganhar pontos
6. Ao final, o ranking de todos os jogadores da sessão é exibido

### Exemplo de execução

```````````````````````````````````````````````````
Nome do Jogador: Player1
JOGO DA ADIVINHAÇÃO
Pontuação atual:  100
Tente adivinhar o número entre 1 e 100
Você tem 10 tentativas
Escolha a dificuldade (fácil/médio/difícil): facil
Digite seu palpite: 50
O número secreto é MENOR
Pontuação atual:  98
Digite seu palpite: 25
O número secreto é MAIOR
Pontuação atual:  96
Digite seu palpite: 32
O número secreto é MENOR
Pontuação atual:  94
Digite seu palpite: 28

 Parabéns! Você acertou!
Pontuação final: 104
Tentativas usadas: 4

 Deseja jogar novamente? (s/n): s
Nome do Jogador: Player2
JOGO DA ADIVINHAÇÃO
Pontuação atual:  100
Tente adivinhar o número entre 1 e 100
Você tem 10 tentativas
Escolha a dificuldade (fácil/médio/difícil): medio
Digite seu palpite: 50
O número secreto é MENOR
Pontuação atual:  95
Digite seu palpite: 25
O número secreto é MENOR
Pontuação atual:  90
Digite seu palpite: 12
O número secreto é MENOR
Pontuação atual:  85
Digite seu palpite: 6
O número secreto é MAIOR
Pontuação atual:  80
Digite seu palpite: 9

 Parabéns! Você acertou!
Pontuação final: 90
Tentativas usadas: 5

 Deseja jogar novamente? (s/n): s
Nome do Jogador: Player3
JOGO DA ADIVINHAÇÃO
Pontuação atual:  100
Tente adivinhar o número entre 1 e 100
Você tem 10 tentativas
Escolha a dificuldade (fácil/médio/difícil): dificil
Digite seu palpite: 50
O número secreto é MAIOR
Pontuação atual:  85
Digite seu palpite: 75
O número secreto é MAIOR
Pontuação atual:  70
Digite seu palpite: 82
O número secreto é MAIOR
Pontuação atual:  55
Digite seu palpite: 91
O número secreto é MAIOR
Pontuação atual:  40
Digite seu palpite: 96
O número secreto é MAIOR
Pontuação atual:  25
Digite seu palpite: 98

 Parabéns! Você acertou!
Pontuação final: 35
Tentativas usadas: 6

 Deseja jogar novamente? (s/n): s
Nome do Jogador: Player4
JOGO DA ADIVINHAÇÃO
Pontuação atual:  100
Tente adivinhar o número entre 1 e 100
Você tem 10 tentativas
Escolha a dificuldade (fácil/médio/difícil): dificil
Digite seu palpite: 50
O número secreto é MENOR
Pontuação atual:  85
Digite seu palpite: 75
O número secreto é MENOR
Pontuação atual:  70
Digite seu palpite: 70
O número secreto é MENOR
Pontuação atual:  55
Digite seu palpite: 30
O número secreto é MAIOR
Pontuação atual:  40
Digite seu palpite: 80
O número secreto é MENOR
Pontuação atual:  25
Digite seu palpite: 65
O número secreto é MENOR
Pontuação atual:  10
Digite seu palpite: 101
O número secreto é MENOR
Pontuação atual:  -5
Digite seu palpite: 30
O número secreto é MAIOR
Pontuação atual:  -20
Digite seu palpite: 50
O número secreto é MENOR
Pontuação atual:  -35
Digite seu palpite: 710
O número secreto é MENOR
Pontuação atual:  -50
Suas tentativas acabaram!
O número secreto era:  42
Pontuação final após perder: -50

 Deseja jogar novamente? (s/n): n
Ranking: 
 1. Player1: 104 pontos
 2. Player2: 90 pontos
 3. Player3: 35 pontos
 4. Player4: -50 pontos
`````````````````````````````````````````````

## Conceitos de POO Utilizados

- **Abstração** — classe `Jogo` define interface comum via `ABC`
- **Herança** — `JogoAdivinhação` estende `Jogo`
- **Encapsulamento** — atributos privados com prefixo `_` (`_numero_secreto`, `_tentativas`, etc.)
- **Polimorfismo** — implementação dos métodos abstratos `iniciar()` e `jogar()`

---

## Melhorias Futuras

- [ ] Salvar ranking em arquivo `.json` ou banco de dados
- [ ] Interface gráfica com `tkinter` ou web com `Flask`
- [ ] Novos modos de jogo (ex: tempo limitado)
- [ ] Testes automatizados com `pytest`

---

##  Licença

Este projeto está sob a licença de Guilherme de Almeida Cavalcante
