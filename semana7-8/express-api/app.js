const express = require('express');
const app = express();

app.use(express.json());

// 1. Rota principal
app.get('/', (req, res) => {
  res.send('API está ativa');
});

// 2. Rota que retorna JSON
app.get('/mensagem', (req, res) => {
  res.json({ mensagem: 'Olá, esta é uma resposta em JSON da API.' });
});

// 3. POST que recebe JSON e valida
app.post('/echo', (req, res) => {
  const body = req.body;

  if (!body || Object.keys(body).length === 0) {
    return res.status(400).json({
      erro: 'Corpo da requisição deve conter um JSON válido.',
    });
  }

  res.status(200).json({
    mensagem: 'JSON recebido com sucesso!',
    dadosRecebidos: body,
  });
});

// 4. Rotas inexistentes
app.use((req, res) => {
  res.status(404).json({
    erro: 'Rota não encontrada',
  });
});

// 5. Porta 3000
const PORT = 3000;

app.listen(PORT, () => {
  console.log(`Servidor Express rodando na porta ${PORT}`);
});
