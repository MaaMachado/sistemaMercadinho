# 🛒Sistema de Mercadinho
Exercício de Python - Criar um Sistema de Mercadinho (Admin e Cliente)

## 👨🏽‍💻**Introdução:**

`Bem-vindo à documentação do sistema de mercado, totalmente na linguagem Python, desenvolvido por Maria Machado como parte do exercício 1 da UC15(Implementação de Inteligência Artificial) do curso Técnico em Desenvolvimento de Sistemas - Senac 22/23. 
Nesta documentação, apresentarei uma visão geral, como acessar esse projeto, seus objetivos e funcionamento final.` <br>
               
---

## ✨ Visão Geral:

O sistema "Mercadinho Crocodile" foi criado para demonstrar e testar os conhecimentos de python, aprendidos em sala de aula, e é um sistema de gerenciamento de um mercadinho fictício localizado no bairro de Brotas, em Salvador. 
<br><br>
Este sistema é dividido em duas partes principais: a parte do cliente e a parte administrativa. Ele permite que os clientes realizem compras de produtos de forma interativa e também oferece funcionalidades de administração para adicionar, editar, ou excluir produtos e categorias.

---

## 💻 Como Acessar o Projeto:

Para acessar e utilizar o Projeto Mercadinho Crocodile, siga as instruções abaixo:

- Clone esse repositório;

  ```
   git clone https://github.com/MaaMachado/sistemaMercadinho.git
   ```

- Abra um terminal no vscode ou prompt de comando do computador;
- Acesse diretamente a pasta do projeto usando o comando `cd`, ou outro, que deve ser chamada "sistemaMercadinho".
- Execute o seguinte comando para iniciar o sistema:

   ```
   python mercado.py
   ```

- Se for para a parte administrativa, você será solicitado a inserir uma senha para acessar-la(a senha é "1234") e se for para a parte de cliente, pode prosseguir sem demora;
- Siga as instruções apresentadas no terminal para prosseguir pelo sistema.


---

## 🏆 Objetivos:

### Parte Administrativa

1. Oferecer funcionalidades de administração para gerenciar categorias de produtos.
2. Permitir adição, edição e exclusão de produtos.
3. Exibir informações detalhadas sobre produtos e categorias.
4. Controlar os preços e as quantidades de produtos disponíveis.
5. Garantir a segurança com uma senha de administrador.

### Parte do Cliente

1. Coletar informações básicas do cliente, como nome, idade e endereço.
2. Permitir que o cliente escolha produtos de diferentes categorias.
3. Manter um carrinho de compras para acompanhar os produtos selecionados.
4. Calcular o valor total da compra, incluindo uma taxa de entrega fixa.
5. Aceitar diferentes métodos de pagamento para concluir a compra.
6. Fornecer uma experiência de compra fácil e intuitiva.


---

## 🖥 Funcionamento do Sitema:


### Parte Administrativa

Atinge todos os objetivos esperados e têm o adicional de:
1. Verificação de informções digitadas, podendo voltar para digitar corretamente depois;
2. Entre outros adicionais.

### Parte do Cliente

Atinge todos os objetivos esperados e têm o adicional de:
1. Verificar se o Cliente reside em Salvador no bairro de Brotas;
2. Estabelecer uma restrição de idade do cliente (para produtos alcoólicos, para menores de idade, e se forem menores de 12 anos);
3. Verificar se o endereço foi digitado corretamente (a rua têm que ter 'Rua' ou 'Avenida' para prosseguir) e se foi digitado mesmo um numeral na parte do número da rua;
4. Confirmação das informações digitadas pelo Cliente, podendo não confirmar e reiniciar o questionário/cadastro;
6. Verificar a disponibilidade dos produtos;
7. Entre outros adicionais.

---

## 💾 Conclusão:

O projeto Mercadinho Crocodile é uma simulação completa de um sistema de gerenciamento e atendimento online para um mercadinho. Ele oferece uma experiência interativa para os clientes e funcionalidades robustas para a administração dos produtos e categorias. Este projeto é um exemplo prático de programação em Python e pode ser adaptado para atender às necessidades específicas de um mercado real.

---
