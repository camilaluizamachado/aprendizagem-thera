# Conversores de Moedas em Python

Este repositório contém dois scripts de conversão de moedas desenvolvidos em Python: um baseado em **taxas fixas** e outro que busca **taxas atualizadas via API**. Ambos servem para prática de Python e manipulação de entradas e saídas do usuário.

---

## 1️⃣ Conversor com Taxas Fixas (`conversor.py`)

**Descrição:**  
Realiza a conversão entre Real, Dólar e Euro usando valores definidos manualmente dentro do código.

**Taxas atuais no script:**
- 1 Dólar = 5.34 Reais  
- 1 Euro = 6.69 Reais  

**Funcionalidades:**
- Converter de Real → Dólar/Euro
- Converter de Dólar/Euro → Real
- Menu interativo com opção de sair
- Tratamento básico de entradas inválidas

**Exemplo de uso:**
Escolha uma operação: 1 - Real para Dólar
Digite o valor em real: 100
100 reais = 18.73 dólares.

**Ponto forte:** Funciona offline, rápido e simples.  
**Limitação:** As taxas não são atualizadas automaticamente.

---

## 2️⃣ Conversor com API (`conversorapi.py`)

**Descrição:**  
Consulta as cotações de moedas em tempo real usando a [AwesomeAPI](https://economia.awesomeapi.com.br/json/last/USD-BRL) para converter valores entre Real, Dólar e Euro.

**Funcionalidades:**
- Consulta ao valor atual do Dólar e do Euro
- Menu interativo com opção de sair
- Recebe valores do usuário e faz a conversão atualizada
- Aceita vírgula ou ponto como separador decimal

**Exemplo de uso:**

Opção: 1
Valor: 100
100 reais = 18.72 dólares (cotação 5.34)

**Ponto forte:** Sempre usa a taxa de câmbio mais recente.  

## Como rodar

1. Instale a biblioteca requests (somente para o script com API):
```bash
pip install requests

Execute o script desejado:

python conversor.py       # Taxas fixas
python conversorapi.py    # API de cotações
