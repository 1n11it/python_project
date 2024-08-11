# dntCARE

## Description
dntCARE is a Flask-based blog application that allows users to create accounts, publish posts, and interact with other users' content. This personal project showcases various features of Flask and demonstrates how to build a functional web application with user authentication and database integration.

## Features
- User authentication (register, login, logout)
- Password reset functionality with email support
- Create, read, update, and delete blog posts
- User profile management (update username, email, and profile picture)
- Responsive web design for various devices

## Project Structure
```
dntCARE/
├── blog/
│   ├── errors/
│   │   └── handlers.py
│   ├── main/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── posts/
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── routes.py
│   ├── static/
│   │   └── profile_pic/
│   ├── templates/
│   │   ├── errors/
│   │   │   ├── 403.html
│   │   │   ├── 404.html
│   │   │   └── 500.html
│   │   ├── account.html
│   │   ├── create_post.html
│   │   ├── home.html
│   │   ├── layout.html
│   │   ├── login.html
│   │   ├── post.html
│   │   ├── register.html
│   │   ├── reset_request.html
│   │   ├── reset_token.html
│   │   └── user_posts.html
│   ├── users/
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   ├── routes.py
│   │   └── utils.py
│   ├── __init__.py
│   ├── config.py
│   └── models.py
├── env/
├── .gitignore
├── requirements.txt
└── run.py
```

## Technologies Used
- Python
- Flask
- Flask-SQLAlchemy
- Flask-Bcrypt
- Flask-Login
- Flask-Mail
- Flask-WTF
- Pillow
- SQLite (for development)

## Installation

1. Clone the repository:
```sh
git clone https://github.com/1n11it/python_project.git
cd python_project/dntCARE
```

2. Create a virtual environment and activate it:
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:
```sh
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory and add the following variables:
```
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///site.db
EMAIL_USER=your_email@example.com
EMAIL_PASS=your_email_password
```

## Usage

1. Run the application:
```sh
python run.py
```

2. Open a web browser and navigate to `http://localhost:5000`

3. Register a new account or log in with existing credentials

4. Start creating and interacting with blog posts!

## Contributing
This is a personal project, but suggestions and feedback are welcome. Feel free to open an issue if you have ideas for improvements or encounter any bugs.

## Contact
For more information or queries, please visit the [repository](https://github.com/1n11it/python_project).
