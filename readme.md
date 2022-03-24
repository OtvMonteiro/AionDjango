# Sistema em Django

##  Tabelas e campos do sistema:
### 1. Produto
nome
imagem
preço unitário
estoque
### 2. Venda (vamos assumir, para simplificar, que uma venda é de um único produto, então não teremos um carrinho com mais de um produto):
email
cpf
nome
endereço
data
id produto
quantidade
valor tota

## Atividades:
### 1. Menu > Gerenciar Produtos (essa tela é como se fosse a tela do dono do site, que ele vai cadastrar seus produtos, estoque, preço, etc):
abre a listagem de produtos.
cadastrar novos
editar (botão na listagem de cada produto)
### 2. Menu > Catálogo (essa tela é como se fosse a tela do cliente navegando no site, vendo um catálogo com os produtos à venda)
Listagem de catálogo de produtos, com foto, para produtos disponíveis apenas.
Botão "comprar" em cada produto, que vai para uma tela para selecionar a quantidade desejada e preencher dados da compra (cpf/email/nome/endereço)
Nessa tela terá um botão "finalizar compra", vai para tela de compra finalizada, com valor total