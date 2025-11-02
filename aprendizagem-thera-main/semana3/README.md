## 📁 Exercícios

### 1️⃣ Calculadora sem interface (`calculadora.py`)

**Descrição:** Calculadora que roda no terminal. O usuário digita a expressão (ex: `2+3*4`) e recebe o resultado. Aceita decimais, inteiros e operações básicas (+, -, *, /).  

**Lógica usada:**  
- `while True` mantém a calculadora ativa até digitar `'sair'`.  
- `input()` captura a expressão do usuário.  
- `eval()` calcula a expressão.  
- Condicional para imprimir números inteiros sem ponto decimal se o resultado for exato.  
- `try/except` trata entradas inválidas.  

**Como rodar:**  
```bash
python calculadora.py

### 2️⃣ Calculadora com interface gráfica (`calculadorab.py`)

**Descrição:**  
Calculadora com GUI usando `Tkinter`. Permite clicar nos botões para digitar números e operações.

**Lógica usada:**  
- Criamos uma janela (`Tk()`) e um campo de entrada (`Entry`) para o visor.  
- Botões com `command` para adicionar números, apagar, limpar ou calcular.  
- `eval()` calcula a expressão ao clicar `=`.  
- Tratamento de erro com `messagebox.showerror`.

**Como rodar:**  
```bash
python calculadorab.py

 ### 3️⃣ Contagem regressiva (`contagemregressiva.py`)

**Descrição:**  
Contagem regressiva a partir de um número digitado pelo usuário até 0.

**Lógica usada:**  
- `input()` captura o número inicial do usuário  
- `while num > 0:` decrementa o número até chegar a zero  
- `print()` mostra cada passo da contagem  

**Como rodar:**  
```bash
python contagemregressiva.py

### 4️⃣ Tabuada (`tabuada.py`)

**Descrição:**  
Gera a tabuada de um número ou de vários números de várias formas.

**Lógica usada:**  
- **For simples:** loop de 1 a 10 multiplicando pelo número  
- **While:** mesma lógica do for, mas usando loop `while`  
- **Função:** encapsula o cálculo da tabuada em `def tabuada(n)`  
- **Tabuada até um número definido pelo usuário**  
- **Tabuada de vários números:** usando dois loops, um para os números e outro para multiplicação  

**Como rodar:**  
```bash
python tabuada.py

## ⚡ Comandos Git usados

```bash
# Inicializar repositório
git init

# Adicionar arquivos ao stage
git add calculadora.py calculadorab.py contagemregressiva.py tabuada.py README.md

# Criar commit com mensagem
git commit -m "Adiciona exercícios de lógica: calculadora, tabuada e contagem regressiva"

# Conectar repositório remoto
git remote add origin <URL_DO_REPOSITORIO>

# Enviar alterações para o GitHub
git push -u origin main

# Criar nova branch
git checkout -b nome-da-branch

# Ver status do repositório
git status
