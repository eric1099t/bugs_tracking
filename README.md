# Bug Tracker API 🐛

A lightweight, RESTful Bug Tracking API built with **FastAPI** and Python. This project demonstrates core backend development concepts including CRUD operations, modular architecture (Separation of Concerns), and data validation.

## 🌟 Features

- **Full CRUD Operations**: Create, Read, Update, and Delete bug tickets efficiently.
- **Data Validation**: Ensures all incoming requests are structurally sound and logically correct using `Pydantic`.
- **Modular Architecture**: Clean separation between the API presentation layer and core business logic.
- **Persistent Storage**: Reads and writes data to a local `jira_data.json` file to maintain state across server restarts.
- **Auto-generated Documentation**: Out-of-the-box Swagger UI for interactive testing.

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Framework**: FastAPI
- **Server**: Uvicorn
- **Validation**: Pydantic

## 📂 Project Structure

- `main.py`: The entry point of the application. It handles API routing, HTTP requests, and responses (The Controller).
- `lesson2.py`: Contains the core business logic, data models (`Bug`, `BugTracker`), and file I/O operations (The Service Layer).
- `jira_data.json`: The local JSON file acting as the database.
- `.gitignore`: Specifies intentionally untracked files to ignore (e.g., `__pycache__`).

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed on your machine. You will also need to install the required libraries:

```bash
pip install fastapi uvicorn pydantic
```


The API will be available at http://127.0.0.1:8000.


Interactive API Docs
Once the server is running, you can test all endpoints directly from your browser by visiting:
👉 http://127.0.0.1:8000/docs
