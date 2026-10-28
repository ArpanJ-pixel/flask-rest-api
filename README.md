Flask REST API

A RESTful API built with Python, Flask, Flask-RESTful, Flask-SQLAlchemy, and SQLite to manage user records.

Features

- Retrieve all users
- Create a new user
- Retrieve a user by ID
- Update user details using PATCH
- Delete a user by ID
- Validate required fields
- Prevent duplicate names and email addresses
- Return appropriate HTTP status codes for common errors
- 
Tech Stack

- Python
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- SQLite

Installation

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ArpanJ-pixel/flask-rest-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flask-rest-api
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```
   On Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Run the Application

```bash
python api.py
```

The development server runs at:

`http://127.0.0.1:5000`

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/users/` | Retrieve all users |
| POST | `/api/users/` | Create a user |
| GET | `/api/users/<id>` | Retrieve a user by ID |
| PATCH | `/api/users/<id>` | Update a user's details |
| DELETE | `/api/users/<id>` | Delete a user |

## Example POST Request

Send a POST request to `/api/users/` with a JSON body:

```json
{
  "name": "Arpan",
  "email": "arpan@example.com"
}
```

## Learning Outcomes

This project demonstrates REST API development, CRUD operations, database integration, request parsing, response serialization, and HTTP status-code handling.
