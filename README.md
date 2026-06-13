# Support CRM Dashboard

A simple Support CRM web application built using FastAPI and SQLite.

## Features

- Create support tickets
- View all tickets
- Search tickets by customer or subject
- Filter tickets by status (Open/Closed)
- View ticket details
- Close tickets
- Delete tickets
- Persistent data storage using SQLite

## Tech Stack

- FastAPI
- Python
- SQLite
- HTML
- CSS
- JavaScript

## How to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Start the server:
   ```
   uvicorn app.main:app --reload
   ```

3. Open your browser and visit:
   ```
   http://127.0.0.1:8000/ui
   ```

## Project Structure

- `app/main.py` – FastAPI routes
- `app/models.py` – Database models
- `app/database.py` – Database configuration
- `templates/index.html` – Frontend UI
- `support_crm.db` – SQLite database