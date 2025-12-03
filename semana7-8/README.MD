# Semana 7–8 – Node.js e Express

Esta semana foi focada em introdução ao Node.js e criação de APIs com Express.

## Conteúdo estudado

- Introdução ao Node.js: o que é, para que serve e principais vantagens.
- Conceitos de servidor HTTP usando apenas o módulo nativo `http`.
- Criação de API REST básica usando o framework Express.
- Uso de JSON em respostas HTTP e tratamento de rotas inexistentes.

## Desafio 1 – Servidor HTTP básico (sem Express)

Arquivos:
- `servidor-http/server.js`

Requisitos implementados:
- Servidor criado com `http.createServer()`.
- Rota `/` retornando texto simples: “Hello, world”.
- Rota `/json` retornando uma resposta em formato JSON.
- Demais rotas retornam status HTTP 404 com mensagem de erro.

Como executar:

cd semana7-8/servidor-http
node server.js


Acessar no navegador:
- http://localhost:3000/
- http://localhost:3000/json

## Desafio 2 – API básica com Express

Arquivos:
- `express-api/app.js`
- `express-api/package.json`

Requisitos implementados:
- Rota GET `/` informando que a API está ativa.
- Rota GET `/mensagem` retornando uma mensagem em formato JSON.
- Rota POST `/echo` que:
  - recebe um JSON no corpo da requisição,
  - faz validação simples,
  - devolve os mesmos dados recebidos.
- Tratamento de rotas inexistentes com status 404 e mensagem em JSON.
- Servidor configurado para rodar na porta 3000.

Instalar dependências e executar:

cd semana7-8/express-api
npm install


Testar rotas:
- GET http://localhost:3000/
- GET http://localhost:3000/mensagem
- POST http://localhost:3000/echo (enviando JSON no corpo da requisição)
