# Python Web Projects

**Two production-grade web applications** built with **Flask** and **Django** demonstrating full-stack Python web development patterns, authentication, database integration, responsive design, and data visualization.

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/flask-2.x-orange)
![Django](https://img.shields.io/badge/django-4.x-green)
![SQLite](https://img.shields.io/badge/database-SQLite-lightgrey)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Abstract

This repository contains two practical web applications that solve real-world problems using different Python web frameworks:

- **dntCARE**: dntCARE is a Flask-based blog application that allows users to create accounts, publish posts, and interact with other users' content. It demonstrates how to build a functional web application with user authentication and database integration.
- **CalorieCrunch**: CalorieCrunch is a Django-based web application that helps users track their calorie intake and provides nutritional information for various foods. It offers suggestions for calorie-burning activities and visualizes nutritional content using interactive charts.

Both projects emphasize clean architecture, proper separation of concerns, security best practices, and user-friendly interfaces.

## Key Features

### dntCARE (Flask)
- Secure user authentication (register / login / logout)
- Password reset via email
- CRUD operations for blog posts
- Profile editing (username, email, picture upload)
- Responsive design (mobile-first)
- Flash messages & form validation

### CalorieCrunch (Django)
- Track daily calorie intake
- Search & add foods with nutritional information
- Interactive charts showing macros & calories (Chart.js)
- Activity suggestions with estimated calorie burn & duration
- Clean class-based views & Django forms
- Responsive UI with Bootstrap

## Tech Stack
<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" height="30"/>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" height="30"/>
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django" height="30"/>
  <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" height="30"/>
  <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap" height="30"/>
  <img src="https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white" alt="Chart.js" height="30"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" height="30"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" height="30"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" height="30"/>
</p>

| Technology          | dntCARE (Flask)                  | CalorieCrunch (Django)                  | Purpose                              |
|---------------------|----------------------------------|-----------------------------------------|--------------------------------------|
| Framework           | Flask                            | Django 4.x / 5.x                        | Web framework                        |
| Database            | SQLite                           | SQLite (PostgreSQL-ready)               | Development & lightweight prod       |
| ORM / DB layer      | SQLAlchemy (optional)            | Django ORM                              | Database abstraction                 |
| Authentication      | Flask-Login + Flask-WTF          | Django Authentication                   | User sessions & security             |
| Forms               | Flask-WTF                        | Django Forms + ModelForms               | Input validation                     |
| Templating          | Jinja2                           | Django Templates                        | HTML rendering                       |
| Styling             | Bootstrap 5 + custom CSS         | Bootstrap 5 + custom CSS                | Responsive layout                    |
| Charts / Visuals    | —                                | Chart.js                                | Data visualization                   |
| Email               | Flask-Mail                       | Django email backend                    | Password reset & notifications       |
| Deployment targets  | Render, Railway, Fly.io, Vercel  | Railway, Render, Fly.io, Heroku         | Easy PaaS hosting                    |

## Project Structure
```
python_project/
├── dntCARE/                    # Flask blog application
│   ├── app/
│   ├── templates/
│   ├── static/
│   ├── migrations/             (if using Flask-Migrate)
│   ├── config.py
│   ├── requirements.txt
│   └── README.md
│
├── CalorieCrunch/              # Django calorie tracker
│   ├── caloriecrunch/          # Django project
│   ├── tracker/                # Main app
│   ├── static/
│   ├── templates/
│   ├── manage.py
│   ├── requirements.txt
│   └── README.md
│
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.9 or higher
- Git
- (Recommended) Virtual environment tool: `venv` (built-in) or `virtualenv`

### 1. Clone the repository
```bash
git clone https://github.com/1n11it/python_project.git
cd python_project
```
### 2. Navigate to the desired project
This repository contains two separate applications. Choose the directory for the project you wish to run:
```bash
#For the Flask application
cd dntCARE
# OR for the Django application
cd "Calorie Tracker"
```
### 3. Individual Project Documentation
Please refer to the individual readme files within each project directory for specific installation and usage instructions.

- [dntCARE](./dntCARE/README.md)
- [CalorieCrunch](./Calorie%20Tracker/README.md)


## License
This project is licensed under the MIT License. Feel free to use the code for learning or personal projects.
