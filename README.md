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

Caso já tenha clonado o repositório, acesse o diretório python-api-test e instale as dependências:

		pip install -r requirements.txt

Se não clonou ainda, efetue:

  		git clone https://github.com/Rafa-Mendes98/Testes-DOT.git

Para executar os testes:

  		python api-test.py

# Questão 3

Para integrar a execução dos testes no pipeline CI/CD usando GitHub Actions, eu configuraria um workflow que disparasse os testes automaticamente sempre que houvesse uma alteração no código, como push ou pull request. Abaixo está um passo a passo sobre como eu estruturaria essa integração:

1. Configuração do GitHub Actions:
   
Primeiro, criaria um arquivo de workflow dentro do diretório .github/workflows, por exemplo, ci.yml. Esse arquivo vai definir as ações do pipeline.

yaml

  		name: CI/CD Pipeline
		on:
		  push:
		    branches:
		      - main
		  pull_request:
		    branches:
		      - main
		jobs:
		  test:
		    runs-on: ubuntu-latest
		    strategy:
		      matrix:
		        node-version: [14, 16]  # Caso o projeto utilize Node.js, ajustaria conforme necessário
		        # Para Python, por exemplo:
		        # python-version: [3.7, 3.8, 3.9]
		    steps:
		    - name: Checkout code
		      uses: actions/checkout@v2
		    - name: Set up Node.js
		      uses: actions/setup-node@v2
		      with:
		        node-version: ${{ matrix.node-version }}
		    - name: Install dependencies
		      run: npm install  # ou pip install para Python
		    - name: Run Tests
		      run: npm test  # ou pytest para Python
      
2. Disparo Automático de Testes:

O pipeline seria disparado automaticamente sempre que uma alteração fosse feita no branch main ou quando um pull request fosse enviado. Isso ocorre com as opções configuradas em on.push e on.pull_request.

3. Garantir que Falhas Sejam Reportadas:
   
O GitHub Actions permite que os resultados dos testes sejam exibidos diretamente na interface do GitHub. Caso haja falhas, elas serão destacadas na execução do workflow. Além disso, posso configurar o status de falha para que seja enviado um alerta para o time ou para um canal de comunicação, como Slack.

yaml

		- name: Notify failure (Slack)
		  if: failure()
		  uses: 8398a7/action-slack@v3
		  with:
		    status: fail
		    slack_webhook_url: ${{ secrets.SLACK_WEBHOOK_URL }}
      
Esse código envia um alerta para o Slack sempre que um teste falha, ajudando a garantir que as falhas sejam rapidamente percebidas.

4. Paralelismo para Rodar Testes Mais Rapidamente:
   
Para otimizar o tempo de execução dos testes, podemos usar o paralelismo, rodando testes em diferentes versões de Node.js ou Python, como mostrei acima no exemplo de matrix. Isso permite que o GitHub Actions execute os testes em múltiplas versões do ambiente de forma simultânea, acelerando a execução.

Além disso, para testes mais complexos, podemos dividir o conjunto de testes em várias partes e distribuí-las para diferentes runners, como:

yaml

		strategy:
		  matrix:
		    test-suite: [unit, integration, ui]
      
Isso dividiria os testes em três grupos distintos e os executaria em paralelo.

5. Relatórios e Logs:

Ao final da execução dos testes, os logs e os relatórios estarão disponíveis diretamente no GitHub Actions, permitindo que eu veja quais testes passaram e quais falharam. Para maior visibilidade, posso integrar com ferramentas como SonarQube ou Test Coverage Reports.

Conclusão:

Esse pipeline automatiza a execução de testes em diferentes cenários e garante que falhas sejam notificadas prontamente. O uso de paralelismo e a integração com ferramentas de notificação ajudam a garantir uma execução eficiente e a comunicação rápida de problemas. A estrutura do workflow no GitHub Actions é simples e clara, mas poderosa, permitindo ajustes conforme necessário para diferentes tipos de testes e ambientes.

# Questão 4

1. Ao testar uma aplicação como o ChatGPT, alguns aspectos principais que eu avaliaria seriam:

- Precisão nas respostas: Verificar se as respostas geradas pela IA são corretas, relevantes e contextualizadas conforme a entrada do usuário. Isso inclui avaliar o modelo de linguagem, seu treinamento e a capacidade de responder adequadamente a uma variedade de perguntas, mantendo a coerência e a lógica.

- Interatividade e fluidez: Testar como a aplicação lida com conversas contínuas e interações com diferentes tipos de perguntas. A IA deve ser capaz de manter um fluxo de conversa natural, sem se perder no contexto, e lidar com interrupções ou mudanças de assunto.

- Escalabilidade e desempenho: Avaliar a capacidade da aplicação de processar múltiplas requisições simultâneas sem perda de desempenho. A aplicação precisa ser eficiente em termos de tempo de resposta, especialmente em situações de alta demanda.

- Compreensão de intenções e contexto: Testar se o modelo consegue entender nuances, intenções e até mesmo sarcasmo ou outras formas de linguagem complexa. A IA deve identificar a intenção por trás da interação, mesmo quando a comunicação não é direta ou clara.

- Detecção e tratamento de falhas: Verificar se o modelo lida bem com entradas inesperadas, erros de digitação, ou perguntas fora do escopo. A IA precisa ser capaz de tratar falhas sem gerar respostas erradas ou sem sentido.

- Segurança e ética: Avaliar como a IA lida com conteúdo sensível ou perguntas inadequadas, garantindo que não haja respostas prejudiciais, preconceituosas ou inseguras.

2. Sim, eu já utilizei ferramentas de IA para testes automatizados.

- Ferramenta: Usei o ChatGPT para gerar casos de teste e scripts automatizados.

- Propósito: Foi aplicada para geração automática de casos de teste, ajudando a criar cenários variados e cobrindo uma ampla gama de entradas que poderiam ser feitas por um usuário. Isso foi particularmente útil para expandir a cobertura de testes de maneira rápida e eficiente.

- Impacto e resultados obtidos: A utilização de ChatGPT na geração de casos de teste aumentou a produtividade, pois a ferramenta ajudou a cobrir mais cenários, incluindo os de difícil previsão. Isso reduziu o tempo de criação manual de testes e proporcionou uma cobertura maior.

3. Mesmo sem ter utilizado IA em todos os aspectos dos testes automatizados, acredito que a Inteligência Artificial pode ser um divisor de águas para a automação de testes. Algumas formas em que a IA pode melhorar esse processo incluem:

- Geração automática de testes: A IA pode gerar cenários de teste automaticamente, identificando as melhores práticas e combinando entradas e condições de teste com base no comportamento observado. Isso pode reduzir o esforço manual na criação de testes, aumentando a cobertura e a eficácia do processo de QA.

- Análise inteligente de resultados: Ferramentas de IA podem ser usadas para analisar os resultados dos testes e identificar padrões de falhas ou inconsistências de forma mais rápida e precisa do que os métodos tradicionais, ajudando a priorizar falhas críticas.

- Otimização de testes com aprendizado de máquina: A IA poderia otimizar o processo de testes, aprendendo com dados históricos de falhas e sugerindo os testes mais críticos a serem executados com base em padrões de erros encontrados em versões anteriores.

- Análise de performance: A IA pode ajudar a analisar o desempenho de sistemas de forma mais precisa, identificando gargalos e padrões de comportamento que poderiam passar despercebidos em testes manuais.

Conclusão: 

Essas aplicações de IA na automação de testes ajudam a reduzir o tempo e os custos com QA, além de melhorar a qualidade do software ao proporcionar testes mais abrangentes, rápidos e inteligentes.
