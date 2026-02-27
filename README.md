# Django XML CRUD Web Service with MySQL

## Project Description

This project is a CRUD (Create, Read, Update, Delete) web service developed using the Django framework and connected to a MySQL database. The system accepts client requests strictly in XML format and returns responses strictly in valid XML format. JSON responses are not used.

This project demonstrates:

- Django project setup using virtual environment (venv)
- MySQL database configuration
- Django model creation and migration
- Full CRUD functionality
- XML request parsing
- XML response generation
- API endpoint testing using Thunder Client
- GitHub version control integration

---

## Technologies Used

- Python 3.x
- Django
- MySQL Server
- mysqlclient / PyMySQL
- Virtual Environment (venv)
- Postman or Thunder Client
- Git and GitHub

---

## Project Structure

```
xmlcrud/
│
├── venv/                 # Virtual environment
├── api/                  # Django app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── xml_utils.py
│
├── xmlcrud/              # Project settings
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/yourusername/xmlcrud.git
cd xmlcrud
```

---

### 2. Create Virtual Environment

```
python -m venv venv
```

Activate virtual environment:

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

### 3. Install Dependencies

```
pip install -r requirements.txt
```

If requirements.txt is missing:

```
pip install django
pip install mysqlclient
pip freeze > requirements.txt
```

---

### 4. Configure MySQL Database

Open MySQL Workbench and run:

```
CREATE DATABASE xmlcrud_db;
```

Open file:

```
xmlcrud/settings.py
```

Edit DATABASES section:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xmlcrud_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

### 5. Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

### 6. Run Server

```
python manage.py runserver
```

Server will run at:

```
http://127.0.0.1:8000/
```

---

## API Endpoints

Base URL:

```
http://127.0.0.1:8000/api/
```

---

## CREATE Student

Endpoint:

```
POST /api/students/create/
```

Request XML:

```
<student>
    <name>John Doe</name>
    <email>john@email.com</email>
    <age>22</age>
</student>
```

Response XML:

```
<response>
    <message>Student created</message>
    <id>1</id>
</response>
```

---

## READ All Students

Endpoint:

```
GET /api/students/
```

Response XML:

```
<students>
    <student>
        <id>1</id>
        <name>John Doe</name>
        <email>john@email.com</email>
        <age>22</age>
    </student>
</students>
```

---

## READ Single Student

Endpoint:

```
GET /api/students/1/
```

Response XML:

```
<student>
    <id>1</id>
    <name>John Doe</name>
    <email>john@email.com</email>
    <age>22</age>
</student>
```

---

## UPDATE Student

Endpoint:

```
PUT /api/students/update/1/
```

Request XML:

```
<student>
    <name>John Updated</name>
    <email>johnupdated@email.com</email>
    <age>23</age>
</student>
```

Response XML:

```
<response>
    <message>Student updated</message>
</response>
```

---

## DELETE Student

Endpoint:

```
DELETE /api/students/delete/1/
```

Response XML:

```
<response>
    <message>Student deleted</message>
</response>
```

---

## Error Handling Example

```
<response>
    <error>Student not found</error>
</response>
```

---

## Testing

This project was tested using:

- Postman
- Thunder Client

The following operations were tested:

- Create student
- Retrieve all students
- Retrieve single student
- Update student
- Delete student
- Invalid XML request
- Invalid student ID

---

## Database Verification

To verify stored data in MySQL, run:

```
USE xmlcrud_db;
SELECT * FROM api_student;
```

---

## Generate requirements.txt

To regenerate requirements file:

```
pip freeze > requirements.txt
```

---

## GitHub Upload Instructions

Initialize Git:

```
git init
git add .
git commit -m "Django XML CRUD with MySQL"
```

Connect to GitHub:

```
git branch -M main
git remote add origin https://github.com/yourusername/xmlcrud.git
git push -u origin main
```

---

## Conclusion

This project successfully implements a Django web service connected to MySQL with full CRUD functionality using XML requests and XML responses. The system demonstrates database integration, XML parsing, API development, and proper testing using Postman or Thunder Client.

---

## Author

Name: John Dave M. Rojo 
Course: BSIT - R13  
Instructor: Aladdin A. Buwanding  
Assignment: Django XML CRUD Web Service with MySQL
