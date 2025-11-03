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

