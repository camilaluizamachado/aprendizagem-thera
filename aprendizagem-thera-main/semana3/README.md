# Exercícios de Lógica de Programação

## Objetivo  
Consolidar lógica de programação e começar a transição do Portugol para Python.

## Soft Skills  
- Autonomia: buscar soluções na internet (StackOverflow, docs).  
- Documentar aprendizados no README pessoal.

## Hard Skills  
- Estruturas básicas: variáveis, condicionais, laços.  
- Funções e modularização.  
- Entrada e saída de dados.

---

## Exercícios

### 1️⃣ Calculadora sem interface (`calculadora.py`)

**Descrição:**  
Calculadora que roda no terminal. O usuário digita a expressão (ex: [translate:2+3*4]) e recebe o resultado. Aceita decimais, inteiros e operações básicas (+, -, *, /).

**Lógica usada:**  
- `while True` mantém a calculadora ativa até digitar `'sair'`.  
- `input()` captura a expressão do usuário.  
- `eval()` calcula a expressão.  
- Condicional para imprimir números inteiros sem ponto decimal se o resultado for exato.  
- `try/except` trata entradas inválidas.

**Como rodar:**  
python calculadora.py

---

### 2️⃣ Calculadora com interface gráfica (`calculadorab.py`)

**Descrição:**  
Calculadora com GUI usando Tkinter. Permite clicar nos botões para digitar números e operações.

**Lógica usada:**  
- Criamos uma janela (Tk()) e um campo de entrada (Entry) para o visor.  
- Botões com command para adicionar números, apagar, limpar ou calcular.  
- `eval()` calcula a expressão ao clicar =.  
- Tratamento de erro com `messagebox.showerror`.

**Como rodar:**  
python calculadorab.py

![Visualização](calculadora9.png)

### 3️⃣ Contagem regressiva (`contagemregressiva.py`)

**Descrição:**  
Contagem regressiva a partir de um número digitado pelo usuário até 0.

**Lógica usada:**  
- `input()` captura o número inicial.  
- `while num > 0:` decrementa o número até zero.  
- `print()` mostra cada passo.

**Como rodar:**  
python contagemregressiva.py

---

### 4️⃣ Tabuada (`tabuada.py`)

**Descrição:**  
Gera a tabuada de um número ou de vários números de várias formas.

**Lógica usada:**  
- `for` simples: loop de 1 a 10 multiplicando pelo número.  
- `while`: mesma lógica do for, mas usando loop while.  
- Função: encapsula o cálculo da tabuada em `def tabuada(n)`.  
- Tabuada até um número definido pelo usuário.  
- Tabuada de vários números usando dois loops: um para os números e outro para multiplicação.

**Como rodar:**  
python tabuada.py

## Comandos Git usados

- `git init`
- `git add` 
- `git commit -m` 
- `git remote add origin` 
- `git push -u origin main`
- `git checkout -b` 
- `git status`


