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

## 📡 API Endpoints

An interactive API documentation (Swagger UI) is available at [http://127.0.0.1:8000/docs] after you start the service.

You can also use `curl` for testing directly from your terminal. *(Tip: Append `| jq` to the commands if you want the JSON output beautifully formatted).*

---

### 1. General & System Status

-   **Check if the API is running (Root endpoint):**
    ```bash
    curl http://127.0.0.1:8000/
    ```

### 2. Reading Bug Data (GET)

-   **Retrieve the list of ALL bugs in the system:**
    ```bash
    curl http://127.0.0.1:8000/all_bugs
    ```

-   **Retrieve Actionable Bugs:**
    *(Returns only CRITICAL bugs that are currently OPEN or IN_PROGRESS and exports a report).*
    ```bash
    curl http://127.0.0.1:8000/actionable-bugs
    ```

-   **Get the total count of CRITICAL bugs:**
    ```bash
    curl http://127.0.0.1:8000/critical-bugs/count
    ```

### 3. Managing Bugs (POST, PUT, DELETE)

-   **Create a new Bug (POST):**
    *(You must provide at least a `ticket_id` in the JSON body).*
    ```bash
    curl -X POST http://127.0.0.1:8000/add-bug \
         -H "Content-Type: application/json" \
         -d '{"ticket_id": "BUG-123", "severity": "CRITICAL", "status": "OPEN"}'
    ```

-   **Update an existing Bug's status (PUT):**
    *(Replace `BUG-123` in the URL with the ID you want to update).*
    ```bash
    curl -X PUT http://127.0.0.1:8000/api/bugs/BUG-123 \
         -H "Content-Type: application/json" \
         -d '{"ticket_id": "BUG-123", "new_status": "CLOSED"}'
    ```

-   **Delete a Bug (DELETE):**
    *(Permanently removes the bug from the system and updates `jira_data.json`).*
    ```bash
    curl -X DELETE http://127.0.0.1:8000/api/bugs/BUG-123
    ```