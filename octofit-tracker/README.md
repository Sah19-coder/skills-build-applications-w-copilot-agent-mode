# Octofit Tracker

## Overview
Octofit Tracker is a Django-based web application designed to help users track their fitness activities and progress. This project provides a robust backend structure to manage user data, workouts, and performance metrics.

## Project Structure
The project is organized as follows:

```
octofit-tracker
├── backend
│   ├── octofit_tracker
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── manage.py
│   └── requirements.txt
├── .vscode
│   └── launch.json
├── .gitignore
└── README.md
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd octofit-tracker
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create Django Project**
   ```bash
   django-admin startproject octofit_tracker
   ```

5. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**
   You can run the Django application using the launch configuration in `.vscode/launch.json`.

## Usage
After setting up the project, you can start the development server and access the application at `http://127.0.0.1:8000/`.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.