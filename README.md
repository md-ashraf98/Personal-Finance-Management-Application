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

finance_management_application/
├── finance_app/
│   ├── migrations/
│   ├── static/
│   │   ├── CSS/
│   │   │   └── style.css         # CSS for styling the frontend
│   ├── templates/
│   │   ├── finance_app/
│   │   │   ├── add_transaction.html    # Template for adding new transactions
│   │   │   ├── edit_transaction.html   # Template for editing transactions
│   │   │   ├── delete_transaction.html # Template for deleting transactions
│   │   │   ├── home.html               # Main dashboard template
│   │   │   ├── registration.html       # Template for user registration
│   │   │   └── cover.html              # Landing page template
│   ├── __init__.py
│   ├── admin.py                  # Django admin configuration
│   ├── apps.py                   # Django app configuration
│   ├── forms.py                  # Forms for user inputs (transactions, registration)
│   ├── models.py                 # Django models for user and transaction data
│   ├── tests.py                  # Unit tests for the application
│   ├── urls.py                   # URL routing for the application
│   └── views.py                  # Backend logic for handling user actions
├── finance_management_application/
│   ├── __init__.py
│   ├── asgi.py                   # ASGI configuration for the project
│   ├── settings.py               # Django settings for the project
│   ├── urls.py                   # Root URL configuration
│   └── wsgi.py                   # WSGI configuration for deployment
├── db.sqlite3                    # SQLite database for storing user and transaction data
├── manage.py                     # Django project management script
├── requirements.txt              # Python packages required for the project


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


