# Personal Finance Management Application  

## 📋 Table of Contents  
- [Introduction](#introduction)  
- [Overview](#overview)  
- [Features](#features)  
- [Requirements](#requirements)  
- [Project Folder Structure](#project-folder-structure)  
- [Usage](#usage)  
- [Conclusion](#conclusion)  

---

## 📖 Introduction  
The **Personal Finance Management Application** is a web-based platform designed to simplify financial management. It enables users to track income and expenses, categorize transactions, and generate detailed financial reports for better financial planning.

---

## 🌟 Overview  
Effective financial management is essential for individuals and organizations. This application provides a user-friendly solution to:  
- Monitor income and expenses.  
- Categorize financial transactions.  
- Generate reports to visualize financial data and make informed decisions.

---

## ✨ Features  
- **Income and Expense Management**: Add, update, and delete transactions with ease.  
- **Transaction Categorization**: Assign categories like Food, Rent, Salary, etc., to transactions.  
- **Financial Reports**: View monthly and yearly summaries of income, expenses, and savings.  
- **Responsive UI**: A clean and intuitive interface for easy navigation and usage.  

---

## ⚙️ Requirements  
To run the project, ensure you have the following installed:  
- **Python** (>= 3.10)  
- **Django** (>= 4.2)  
- **SQLite** (default Django database)
-  **Front-End Technologiese** (HTML, CSS)


## ⚙️ Project Folder  

# Project Folder Structure

finance_management_application/
├── finance_app/
│   ├── migrations/                          # Database migrations
│   ├── static/                              # Static files like CSS, JS
│   │   ├── CSS/
│   │   │   └── style.css                    # Custom styles for the frontend
│   ├── templates/                           # HTML templates
│   │   ├── finance_app/
│   │   │   ├── add_transaction.html         # Form to add new transaction
│   │   │   ├── edit_transaction.html        # Form to edit existing transaction
│   │   │   ├── delete_transaction.html      # Page to confirm deletion of transaction
│   │   │   ├── home.html                    # Main dashboard page
│   │   │   ├── registration.html            # Registration page for new users
│   │   │   └── cover.html                   # Cover page for the application
│   ├── __init__.py                           # Mark the directory as a Python package
│   ├── admin.py                              # Admin configurations for the app
│   ├── apps.py                               # App configuration
│   ├── forms.py                              # Form classes for transactions and user registration
│   ├── models.py                             # Database models for transactions and users
│   ├── tests.py                              # Tests for the app's functionality
│   ├── urls.py                               # URL routing for the app
│   └── views.py                              # Logic for handling requests and rendering views
├── finance_management_application/          # Main Django project folder
│   ├── __init__.py                           # Initialize the project
│   ├── asgi.py                               # ASGI configuration for asynchronous support
│   ├── settings.py                           # Settings for the Django project
│   ├── urls.py                               # Main URL routing for the project
│   └── wsgi.py                               # WSGI configuration for deployment
├── db.sqlite3                                # SQLite database file
├── manage.py                                 # Django project management script
└── requirements.txt                          # List of required Python packages


### Install Dependencies  
Install all required dependencies using:  
```bash
pip install -r requirements.txt
```

### Usage
## Running the Project

1. **Clone the repository to your local machine:**
   ```bash
   git clone https://github.com/your-username/finance_management_application.git
   cd finance_management_application
   ```

1. **Set up a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
 ```

1. **Install dependencies:**
   
```bash
pip install -r requirements.txt
Run database migrations:
```

1. **Run database migrations:**
   
```bash
python manage.py migrate
Run the development server:
```

1. **Run the development server:**

```bash
python manage.py runserver
Access the application in your browser: Open your browser and navigate to:
```

1. **Access the application in your browser:**

```bash
http://127.0.0.1:8000/
```


