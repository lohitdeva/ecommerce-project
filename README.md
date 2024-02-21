# E-Commerce Website for Local Store

This project is an e-commerce website designed for local stores to showcase their products online. Built with Django and Flask, it provides a robust platform for store owners to manage their inventory and for customers to browse and purchase products seamlessly. The website features an admin panel for store management and a user-friendly storefront for customer interaction.

## Features

### Admin Panel
- **Secure Login**: Authentication for store owners to access the admin dashboard.
- **Product Management**: Interface to add, edit, and delete product listings, including images, titles, descriptions, and other relevant information.
- **Order Management**: Overview of orders with details on customer purchases and shipping status.
- **Review Management**: Access to customer reviews for each product, with options to respond or moderate.

### Storefront
- **Product Browsing**: Intuitive navigation through product categories and detailed product pages.
- **Shopping Cart**: Functionality to add products to a cart and modify quantities before checkout.
- **Checkout Process**: Secure checkout process including customer information, shipping details, and payment integration.
- **Product Reviews**: Option for customers to leave reviews on products they've purchased.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Django (Admin Panel), Flask (Storefront)
- **Database**: PostgreSQL
- **Authentication**: Django’s built-in authentication for secure login
- **Other Technologies**: Docker (optional for containerization), Git for version control

## Getting Started

### Prerequisites

- Python 3.8 or above
- pip and virtualenv
- PostgreSQL

### Setup

1. **Clone the Repository**

```bash
git clone https://github.com/lohitdeva/ecommerce-project.git
cd ecommerce-project
```

2. **Create and Activate Virtual Environment**

```bash
virtualenv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Setup PostgreSQL**

- Ensure PostgreSQL is installed and running.
- Create a database for the project.

5. **Environment Variables**

- Copy `.env.example` to `.env` and update it with your database credentials and other settings.

6. **Migrate Database**

```bash
python manage.py migrate
```

7. **Run the Development Server**

- Admin Panel (Django)

```bash
python manage.py runserver
```

- Storefront (Flask)

```bash
export FLASK_APP=storefront
export FLASK_ENV=development
flask run
```

8. **Access the Website**

- Admin Panel: Navigate to `http://localhost:8000/admin`
- Storefront: Navigate to `http://localhost:5000`

## Contributing

We welcome contributions to this project! Please consider the following guidelines before submitting your contribution:

- **Fork the Repository**: Start by forking the project repository.
- **Feature Branch**: Create a new branch for each feature or bugfix.
- **Commit Messages**: Write clear, concise commit messages, including a brief description of the changes and the issue number if applicable.
- **Pull Requests**: Submit pull requests against the main branch. Include a clear description of the changes and any relevant issue numbers.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
