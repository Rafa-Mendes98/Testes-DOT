Cypress.Commands.add('searchItemByName', (itemName) => {
    // Busca item:
    cy.get('#twotabsearchtextbox').type(`${itemName}{enter}`);
    // Clica no item:
    cy.get('[data-component-type="s-search-result"]').first().contains(itemName).click();
});

