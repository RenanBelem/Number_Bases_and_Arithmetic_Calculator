## Calculadora de Bases Numéricas e Aritmética (Python - Console)

Este projeto em Python implementa uma calculadora interativa via console focada em **conversão de bases numéricas** e **operações aritméticas** (soma e subtração) entre números de bases diferentes.

### 🎯 Funcionalidades

O programa apresenta um menu principal com três opções principais:

| Opção | Funcionalidade |
| :---: | :--- |
| **1** | Conversão de Base Numérica (Binário, Octal, Decimal, Hexadecimal) |
| **2** | Soma ou Subtração entre dois números de bases diferentes |
| **3** | Sair do programa |

---

### 1. Conversão de Base Numérica (Opção 1)

O usuário pode converter um número entre qualquer par das quatro bases principais: **Binária (2), Octal (8), Decimal (10)** e **Hexadecimal (16)**.

#### Fluxo de Conversão:
1.  O usuário escolhe a **Base Inicial** (1 a 4).
2.  O usuário escolhe a **Base Final** (1 a 4).
3.  O programa solicita o número de entrada na Base Inicial.
4.  O número é **convertido internamente para Decimal** primeiro (`int(n, base)`).
5.  O resultado em Decimal é então convertido para a Base Final desejada usando as funções nativas do Python (`bin()`, `oct()`, `hex()`).

#### Tratamento de Números Negativos
O script trata corretamente números negativos em todas as bases, removendo o prefixo negativo que as funções Python adicionam (ex: `bin(resultado)[3:]` em vez de `[2:]`).

---

### 2. Soma e Subtração entre Bases (Opção 2)

Esta funcionalidade permite realizar uma operação aritmética com dois números que podem estar em bases diferentes.

#### Fluxo da Operação:
1.  O usuário escolhe a operação: **Somar (1)** ou **Subtrair (2)**.
2.  O usuário insere a **Base** e o **Valor** do **primeiro** número.
3.  O usuário insere a **Base** e o **Valor** do **segundo** número.
4.  Ambos os números são **convertidos para Decimal** internamente.
5.  A operação (soma ou subtração) é realizada em Decimal.

#### 📝 Saída do Resultado
O **resultado final** da operação é apresentado em **todas as quatro bases** (Binário, Octal, Decimal e Hexadecimal).

---

### 💻 Execução

O programa roda em um *loop* `while True` no console, garantindo que o usuário possa realizar múltiplas operações até escolher a opção '3' (Sair).
