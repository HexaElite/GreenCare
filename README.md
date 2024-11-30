# GreenCare Django Web Application Project

## Overview
...

## Features
...

## Requirements

- Python 3.x
- Django 3.x or higher

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/HexaElite/GreenCare.git
   cd GreenCare
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   - Update the database settings in `settings.py`.
   - Run migrations:

   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional):**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   Your application should now be running at `http://127.0.0.1:8000/`.


## Django Terminal Commands Guide

Here are some commonly used Django terminal commands that will help you manage your project:

### Project Management

- **Create a new Django project:**
  ```bash
  django-admin startproject projectname
  ```

- **Create a new Django app:**
  ```bash
  python manage.py startapp appname
  ```

### Database Management

- **Run migrations:**
  ```bash
  python manage.py migrate
  ```

- **Create new migrations for changes in models:**
  ```bash
  python manage.py makemigrations
  ```

- **View the current database schema:**
  ```bash
  python manage.py showmigrations
  ```

### Development Server

- **Run the development server:**
  ```bash
  python manage.py runserver
  ```

- **Run the development server on a specific port:**
  ```bash
  python manage.py runserver 8080
  ```

### User Management

- **Create a superuser:**
  ```bash
  python manage.py createsuperuser
  ```

- **Change a user's password:**
  ```bash
  python manage.py changepassword username
  ```

### Testing

- **Run tests:**
  ```bash
  python manage.py test
  ```

### Shell

- **Open the Django shell:**
  ```bash
  python manage.py shell
  ```

### Static Files

- **Collect static files for production:**
  ```bash
  python manage.py collectstatic
  ```
