# Bike Shop

Web project using Django.

## About

**Objective:** Create a template for building a page with featured items.

**Design:** The page features a centered navbar with three cards below, using Yamaha motorcycle photos as placeholders.

**Note:** The project does not include a database. It is up to the user to set up this part.

## Technologies Used

- **[Django](https://www.djangoproject.com/):** Web framework for backend development.  
- **[Bootstrap](https://getbootstrap.com/):** Used for styling and responsive layout.  

## Prerequisites

Before starting, ensure you have the following tools installed on your machine:

- **IDE:** It's good to have a code editor, such as [VSCode](https://code.visualstudio.com/).  
- **Python:** Download it [here](https://www.python.org/downloads/).  
- **Django:** Install it by running `pip install django` in your IDE's terminal.  

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/pachzn/post-shop.git

## Secret Key
The `SECRET_KEY` in Django is used for cryptographic operations and must be kept secret. You can configure it by creating a `.env` file in the project's root directory with the following content:

```env
DJANGO_SECRET_KEY=your-very-secret-key
