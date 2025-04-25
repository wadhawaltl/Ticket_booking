# Ticket Booking Management System

## Project Overview
The Ticket Booking Management System is a web application built using Django. It allows users to view available shows/events, book tickets, and view their booking history. Admins can manage shows (add/edit/delete) and view all bookings through a custom admin panel.

## Setup & Run Instructions

### Prerequisites
- Python 3.10 or higher
- Docker and Docker Compose
- Jenkins (optional for CI/CD)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ticket_booking
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

5. Access the application at `http://127.0.0.1:8000/`.

6. To populate the database with sample shows, run:
   ```bash
   python manage.py populate_shows
   ```

### Using Docker
1. Build and run the application:
   ```bash
   docker-compose up --build
   ```

2. Access the application at `http://127.0.0.1:8000/`.

### Using Jenkins
1. Add the repository to Jenkins.
2. Use the provided `Jenkinsfile` for CI/CD pipeline configuration.

## Tech Stack Used
- **Backend**: Django
- **Database**: SQLite (default), PostgreSQL (via Docker)
- **Frontend**: HTML, CSS
- **Containerization**: Docker, Docker Compose
- **CI/CD**: Jenkins

## Notes
- Ensure Docker and Docker Compose are installed for containerized deployment.
- Use the `Jenkinsfile` for automated build, test, and deployment pipelines.