# FastAPI Product API

A backend REST API project built using FastAPI and Python.
This project provides product management functionality with CRUD operations, validation, and JSON-based data storage.

---

## Features

* Create Product
* Read Product
* Update Product
* Delete Product
* FastAPI Swagger Documentation
* Pydantic Data Validation
* JSON File Storage
* Clean Project Structure

---

## Tech Stack

* Python
* FastAPI
* Uvicorn
* Pydantic

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Move to project directory:

```bash
cd YOUR_REPOSITORY
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Project

```bash
uvicorn main:app --reload
```

Server URL:

```bash
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI:

```bash
http://127.0.0.1:8000/docs
```

ReDoc:

```bash
http://127.0.0.1:8000/redoc
```

---

## Project Structure

```bash
project/
│
├── main.py
├── models/
├── routes/
├── services/
├── data/
├── requirements.txt
└── README.md
```

---

## Future Improvements

* Database Integration
* Authentication & Authorization
* Docker Support
* Deployment
* AI-based Features

---

## Author

Pushpendra
