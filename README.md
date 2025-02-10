# Testes-DOT

Este repositório contém a resolução das questões do Teste da DOT, além do README tradicional para executar os testes, irei incluir as resoluções com mais detalhes e responder as questões 3 e 4.

# Questão 1

Validar a funcionalidade de adicionar um livro ao carrinho no site da Amazon Brasil.

Descrição do Teste:

O teste automatizado simula a busca e adição do livro "AI Engineering: Building Applications with Foundation Models" ao carrinho de compras. 

Ele realiza as seguintes etapas:

- Acessa a página inicial da Amazon Brasil.
- Busca pelo nome do livro.
- Valida as informações do produto, como:
- - Edição em inglês;
- - Autor correto;
- - Formato físico e novo.
- Adiciona o livro ao carrinho de compras.
- Verifica se a mensagem de sucesso "Adicionado ao carrinho" é exibida.

Requisitos:

Node.js: A versão recomendada é a 16.x ou superior.
Cypress: Para executar os testes automatizados.

Passos para Rodar o Teste:

- Clonar o repositório:

		git clone https://github.com/Rafa-Mendes98/Testes-DOT.git

- Instalar dependências:

Navegue até o diretório cypress-amazon-test e instale as dependências necessárias.

		npm install

- Executar os testes:

Para rodar os testes automatizados, use o comando.

		npx cypress open

Isso abrirá a interface do Cypress, onde você poderá selecionar os testes para rodar.

Alternativamente, para rodar os testes em modo headless (sem interface gráfica):

		npx cypress run

# Questão 2

Validar api fornecida com um conjunto de testes.

Descrição dos testes:

1. Teste GET

Este teste realiza uma requisição GET para a URL https://jsonplaceholder.typicode.com/posts, que retorna uma lista de posts. As validações incluem:
- Verificação de que a resposta tem o status HTTP 200;
- Validação de que o retorno é um JSON válido e que o conteúdo é uma lista;
- Verificação de que cada item na lista de posts contém as chaves esperadas: userId, id, title, e body.

2. Teste POST

Este teste realiza uma requisição POST para a mesma URL, criando um novo post com dados aleatórios. As validações incluem:
- Verificação de que a resposta tem o status HTTP 201;
- Validação de que o campo id foi gerado na resposta;
- Verificação de que os dados enviados no POST (title e body) são consistentes com os dados retornados pela API;
- Validação de que o ID gerado pela API é único.

3. Teste de ID Único

Após cada requisição POST, o ID gerado é verificado para garantir que a API está criando IDs únicos. Se o ID gerado já foi retornado em uma requisição anterior, o teste falha.

Requisitos:

Python 3.X - Biblioteca Requests.

Passos para rodar os testes:

Caso já tenha clonado o repositório, acesse o diretório python-api-test e execute:

		python api-test.py

Se não clonou ainda, efetue:

  		git clone https://github.com/Rafa-Mendes98/Testes-DOT.git
