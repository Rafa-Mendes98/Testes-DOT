# Testes-DOT

# Questão 1

Este repositório contém um teste automatizado desenvolvido com Cypress para validar a funcionalidade de adicionar um livro ao carrinho no site da Amazon Brasil.

	Descrição do Teste

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

	Requisitos

Node.js: A versão recomendada é a 16.x ou superior.
Cypress: Para executar os testes automatizados.

	Passos para Rodar os Testes

- Clonar o repositório:

git clone https://github.com/seu-usuario/nome-do-repositorio.git

- Instalar dependências:

Navegue até o diretório do projeto e instale as dependências necessárias.

cd nome-do-repositorio
npm install

- Executar os testes:

Para rodar os testes automatizados, use o comando.

npx cypress open

Isso abrirá a interface do Cypress, onde você poderá selecionar os testes para rodar.

Alternativamente, para rodar os testes em modo headless (sem interface gráfica):

npx cypress run
