# App Name - BookTracker

BookTracker is a Django-based web application that allows users to search for books using the Google Books API, save favorite books, and manage their own personal library. It includes user registration and authentication, a dashboard to view saved books, and a REST API for CRUD operations on books.


## Features

Search for books via Google Books API  
Save books to your personal library  
View, update, and delete your saved books 
Django REST API endpoints for book operations  
User dashboard  for visualization of the data fetched
Responsive HTML templates for search and dashboard pages

## Project Structure

booktracker/
├── books/
│ ├── templates/books/
│ │ ├── book_list.html
│ │ ├── book_search.html
│ │ └── dashboard.html
│ ├── migrations/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── urls.py
│ ├── utils.py
│ └── views.py
├── booktracker/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── .env.txt
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt

# Setup

### 1. Clone the repository


git clone <your-repo-url>
cd booktracker

### 2. Create and activate a virtual environment
On macOS/Linux:

python3 -m venv env
source env/bin/activate

On Windows:

python -m venv env
env\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Create a .env file
You can either copy the existing .env.txt file or create a new .env:

cp .env.txt .env
Edit .env and set your secret key, debug, and database settings if needed.

### 5. Apply database migrations

python manage.py makemigrations
python manage.py migrate

### 6. Create a superuser account

python manage.py createsuperuser
Follow the prompts to set username, email, and password.

### 7. Run the development server

python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.

## Application URLs
Search Books: /search/
Save Book: /save/
My saved Books : /my-books/
Dashboard: /dashboard/

API endpoints: /api/books/
List/Create: GET/POST /api/books/
Update: PUT /api/books/<book_id>/
Delete: DELETE /api/books/<book_id>/


## API Endpoints & Manual Verification
API is served under /api/books and provides full CRUD operations:

Method    Endpoint              Purpose
GET       /api/books/           List all books
POST      /api/books/           Add a new book
GET       /api/books/<id>/      Retrieve a book
PUT       /api/books/<id>/      Update a book
DELETE    /api/books/<id>/      Delete a book

## Environment Variables
.env file should include at least:
GOOGLE_BOOKS_API_KEY=your-api-secret
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=your_db_host
DATABASE_PORT=your_db_port


### Testing your application
You can run unit tests using Django’s test runner:
python manage.py test