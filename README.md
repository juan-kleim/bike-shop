# Bike Shop

Projeto web utilizando Django.

## Sobre

Objetivo: criar um template base para montar uma página com itens em destaque.

Desenho: o site possui uma navbar centralizada com três cards logo abaixo, utilizando fotos de motos Yamaha como padrão.

Obs: o projeto está sem um banco de dados incluído. Cabe ao usuário essa etapa.

## Tecnologias Utilizadas

- **[Django](https://www.djangoproject.com/):** Framework web para desenvolvimento do backend.
- **[Bootstrap](https://getbootstrap.com/):** Utilizado para estilização e layout responsivo.


## Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

- IDE | É bom ter um editor para trabalhar com o código, como [VSCode](https://code.visualstudio.com/).
- Python | Faça o download por [aqui](https://www.python.org/downloads/).
- Django | Digite "pip install django" no terminal da sua IDE.

## Instalação

1. Clone este repositório:
   ```bash
   git clone https://github.com/pachzn/post-shop.git

## Secret Key
A `SECRET_KEY` do Django é usada para fornecer criptografia e deve ser mantida em segredo. Você pode configurar a `SECRET_KEY` criando um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
DJANGO_SECRET_KEY=your-very-secret-key
