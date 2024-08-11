# CalorieCrunch

## Description
CalorieCrunch is a web application built with Django that helps users track their calorie intake and provides nutritional information for various foods. It also offers suggestions for calorie-burning activities and visualizes nutritional content using interactive charts.

## Features
- Food calorie tracking
- Nutritional content lookup for entered food items
- Visualization of nutritional data using Chart.js
- Suggestions for calorie-burning activities with estimated time periods
- User-friendly interface for easy calorie management

## Technologies Used
- Python
- Django
- HTML
- CSS
- JavaScript
- Chart.js

## Project Structure
```
CopyCalorie Tracker/
│
├── CalorieCrunch/
│   ├── __pycache__/
│   ├── static/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── counter/
│   ├── __pycache__/
│   ├── migrations/
│   ├── templates/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── static/
│   ├── admin/
│   ├── images/
│   └── style.css
│
├── .gitignore
├── db.sqlite3
├── manage.py
└── requirements.txt
├── manage.py
└── vercel.json
```

## Installation

1. Clone the repository:
```sh
Copygit clone https://github.com/1n11it/python_project.git
```

2. Navigate to the project directory:
```sh
cd python_project/Calorie\ Tracker
```

4. Create a virtual environment and activate it:
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

5. Install the required packages:
```sh
pip install -r requirements.txt
```

6. Run migrations:
```sh
python manage.py migrate
```

7. Create a superuser (optional):
```sh
python manage.py createsuperuser
```

## Usage
1. Start the development server:
```sh
python manage.py runserver
```

2. Open a web browser and go to:
```sh
http://127.0.0.1:8000/
 ```  
3. Use the interface to enter food items and track your calorie intake.
   
4. Explore nutritional information and calorie-burning suggestions.

## Contributing
This is a personal project, but suggestions and feedback are welcome. Feel free to open an issue if you have ideas for improvements or encounter any bugs.

## Contact
For more information or queries, please visit the [repository](https://github.com/1n11it/python_project).
