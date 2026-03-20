# 🎮 Jogo da Adivinhação em Python

Este projeto é um jogo simples de adivinhação desenvolvido em Python, utilizando conceitos de **Programação Orientada a Objetos (POO)** e **classes abstratas**.

---

## Funcionalidades

* Sistema de jogador com nome e pontuação
* Jogo de adivinhação com número aleatório
* Limite de tentativas
* Sistema de pontuação dinâmica
* Ranking de jogadores ordenado por pontos

---

## Conceitos utilizados

* Classes e objetos
* Herança
* Classe abstrata (`ABC`)
* Encapsulamento
* Tratamento de exceções (`try/except`)
* Ordenação com `lambda`

---

## Estrutura do Código

### Classe `Jogo` (Abstrata)

Define a estrutura base para qualquer jogo:

* `iniciar()`
* `jogar()`

---

### Classe `Jogador`

Representa o jogador:

* `nome`: inserido pelo usuário
* `pontos`: inicia com 100

---

### Classe `Ranking`

Gerencia os jogadores:

* Adiciona jogadores
* Ordena por pontuação
* Exibe ranking

---

### Classe `JogoAdivinhação`

Herda de `Jogo` e implementa a lógica do jogo:

* Gera um número secreto aleatório entre 1 e 100
* Limite de 10 tentativas
* A cada erro:

  * Dica: maior ou menor
  * Penalidade: -2 pontos
* Acerto:

  * +10 pontos

---

## Como executar

1. Certifique-se de ter o Python instalado
2. Salve o código em um arquivo, por exemplo:

```bash
jogo_adivinhacao.py
```

3. Execute no terminal:

```bash
python jogo_adivinhacao.py
```

---

## Como jogar

1. Digite seu nome
2. Tente adivinhar o número entre **1 e 100**
3. Você tem **10 tentativas**
4. Receberá dicas após cada tentativa
5. Sua pontuação muda conforme seu desempenho

---

## Sistema de Pontuação

| Ação            | Pontos |
| --------------- | ------ |
| Acertar número  | +10    |
| Errar tentativa | -2     |

---

## Ranking

Ao final do jogo:

* O jogador é adicionado ao ranking
* Os jogadores são ordenados por pontuação
* O ranking é exibido no console

---

## Melhorias que serão feitas

* Suporte a múltiplos jogadores
* Salvar ranking em arquivo
* Interface gráfica (GUI)
* Níveis de dificuldade
* Repetição de partidas

---

## Autor

Guilherme de Almeida Cavalcante

---
