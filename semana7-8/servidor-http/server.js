const http = require('http');

const server = http.createServer((req, res) => {
  console.log(`${req.method} ${req.url}`);

  if (req.url === '/' && req.method === 'GET') {
    res.writeHead(200, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end('Hello, world');
  } else if (req.url === '/json' && req.method === 'GET') {
    const data = { message: 'Olá, isso é um JSON!', ok: true };
    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
    res.end(JSON.stringify(data));
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
    res.end('404 - Rota não encontrada');
  }
});

const PORT = 3000;

server.listen(PORT, () => {
  console.log(`Servidor HTTP básico rodando na porta ${PORT}`);
});
