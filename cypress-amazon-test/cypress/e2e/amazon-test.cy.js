describe('Questão 1', () => {
  beforeEach(() => {
    cy.visit('https://www.amazon.com.br/');
  });

  it('CT01 - Adicione o livro no carrinho', () => {
    // Define nome do livro:
    const bookName = 'AI Engineering: Building Applications with Foundation Models';
    // Busca item:
    cy.searchItemByName(bookName);
    // Valida que é a edição em inglês e autor correto:
    cy.get('#bylineInfo').should('include.text', 'Edição Inglês')
      .and('include.text', 'Chip Huyen');
    // Valida que é um livro físico e novo:
    cy.get('#productSubtitle').should('include.text', 'Capa comum – 7 janeiro 2025');
    cy.contains('Novo').should('exist');
    // Adicionar ao carrinho:
    cy.get('#add-to-cart-button').click();
    // Validar mensagem de sucesso:
    cy.contains('Adicionado ao carrinho').should('be.visible');
  });
});
