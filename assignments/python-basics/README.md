
# 📘 Assignment: Python Basics

## 🎯 Objetivo

Praticar conceitos fundamentais de Python: entrada do usuário, formatação de strings, operações aritméticas e estruturas condicionais implementando funções simples e testáveis.

## ⏳ Duração estimada

30–45 minutos

## 🔧 Recursos fornecidos

- Código inicial: `starter-code.py`
- Arquivos de apoio/exemplos: veja a pasta da atividade

## 📝 Tarefas

### 🛠️ 1 — Mensagem de boas-vindas

#### Descrição
Implemente `welcome_message()` que solicita nome, idade e cor favorita e retorna uma mensagem formatada.

#### Requisitos

- Ler `name`, `age` e `color` via `input()`.
- Retornar a string: "Hello, [name]! You are [age] years old and your favorite color is [color]."
- Fornecer um exemplo de uso no `if __name__ == '__main__':`.

### 🛠️ 2 — Soma de dois números

#### Descrição
Implemente `add_two_numbers()` que lê dois números do usuário e retorna a soma.

#### Requisitos

- Solicitar dois números (aceitar inteiros ou floats).
- Retornar o resultado (não imprimir diretamente em funções que serão testadas).
- Incluir tratamento básico de entradas inválidas (ex.: mensagens de erro).

### 🛠️ 3 — Verificador de paridade

#### Descrição
Implemente `is_even(n)` que verifica se um número inteiro é par.

#### Requisitos

- Receber um inteiro como argumento.
- Retornar `True` se for par, `False` caso contrário.
- Incluir exemplos no README e testes simples no `starter-code.py`.

## Exemplos

Exemplo de uso de `is_even`:

```python
print(is_even(4))  # True
print(is_even(5))  # False
```

## Como testar

1. Abra um terminal na pasta da atividade.
2. Execute:

```bash
python3 starter-code.py
```

## Observações para o instrutor

- Mantenha o `starter-code.py` pequeno e focado em invocar as funções para facilitar testes automatizados.


