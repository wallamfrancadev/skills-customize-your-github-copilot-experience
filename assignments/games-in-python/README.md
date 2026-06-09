
# 🎮 Hangman (Jogo da Forca)

## 🎯 Objetivo

Construir a versão clássica do jogo da forca em Python, praticando manipulação de strings, loops, condicionais e entrada do usuário.

## ⏳ Duração estimada

60–90 minutos

## 🔧 Recursos fornecidos

- Código inicial: `starter-code.py`
- Lista de palavras exemplo (interna ao `starter-code.py`)

## 📝 Tarefas

### 🛠️ 1 — Seleção de palavra e estado do jogo

#### Descrição
Escolher aleatoriamente uma palavra de uma lista e manter o estado atual (letras reveladas e letras erradas).

#### Requisitos

- Selecionar uma palavra aleatória a partir de uma lista predefinida.
- Representar o progresso do jogador no formato `_ _ a _ _`.

### 🛠️ 2 — Entrada do jogador e lógica de tentativas

#### Descrição
Aceitar guesses do jogador, atualizar o estado e controlar o número de tentativas restantes.

#### Requisitos

- Aceitar entrada de uma letra por tentativa.
- Ignorar entradas inválidas (mais de uma letra, não-alfabético) com mensagem de erro.
- Atualizar letras corretas e lista de erros; decrementar tentativas quando a letra não existir na palavra.

### 🛠️ 3 — Condições de vitória/derrota e mensagens

#### Descrição
Detectar fim de jogo (palavra completa ou tentativas esgotadas) e exibir mensagens apropriadas.

#### Requisitos

- Mostrar mensagem de vitória com a palavra completa quando o jogador acertar todas as letras.
- Mostrar mensagem de derrota quando as tentativas acabarem, revelando a palavra correta.

### 🛠️ 4 — (Opcional) Melhorias

#### Sugestões

- Permitir adivinhar a palavra inteira.
- Salvar pontuações simples (tentativas restantes) em um arquivo.
- Melhorar a interface textual (desenho da forca em ASCII).

## Exemplos / Uso

Execute `starter-code.py` na pasta da atividade para jogar a versão de exemplo:

```bash
python3 starter-code.py
```

## Como testar

- Testes manuais: jogue algumas partidas, verifique tratamento de entradas inválidas e mensagens finais.
- Para facilitar testes automatizados, mantenha a lógica principal em funções (ex.: `select_word()`, `process_guess(state, guess)`).

## Observações para o instrutor

- O `starter-code.py` deve apenas orquestrar a execução e chamar funções testáveis; evite intercalar lógica e I/O intensivo diretamente nas funções core.

