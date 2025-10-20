# OctoFit Tracker Backend

Welcome to the OctoFit Tracker backend! This project is designed to provide a robust backend for the OctoFit Tracker application, which includes features such as user authentication, activity logging, team management, and personalized workout suggestions.

## Project Structure

The backend of the OctoFit Tracker application is organized as follows:

```
octofit-tracker/
├── backend/
│   ├── venv/                     # Python virtual environment
│   ├── requirements.txt           # Required Python packages
│   ├── octofit_tracker/           # Django project directory
│   │   ├── manage.py              # Command-line utility for Django
│   │   ├── octofit_tracker/       # Main application package
│   │   │   ├── __init__.py        # Marks the directory as a Python package
│   │   │   ├── settings.py        # Django settings and configuration
│   │   │   ├── urls.py            # URL routing for the application
│   │   │   ├── asgi.py            # ASGI entry point
│   │   │   └── wsgi.py            # WSGI entry point
│   └── README.md                  # Documentation for the backend
├── frontend/                      # Frontend directory (to be implemented)
│   ├── README.md                  # Documentation for the frontend
│   └── (frontend-src-placeholder)  # Placeholder for frontend source code
└── .vscode/                       # VS Code configuration
    └── launch.json                # Launch configuration for the Django app
```

## Getting Started

### Prerequisites

- Python 3.x
- Django 4.1.7
- Other dependencies listed in `requirements.txt`

### Setting Up the Environment

1. **Create a Python Virtual Environment**:
   Navigate to the `backend` directory and create a virtual environment:
   ```
   python3 -m venv venv
   ```

2. **Activate the Virtual Environment**:
   ```
   source venv/bin/activate
   ```

3. **Install Required Packages**:
   Install the dependencies listed in `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

To run the Django application, use the following command:
```
python manage.py runserver
```

### Additional Information

For more details on the frontend, please refer to the `frontend/README.md` file. 

For any issues or contributions, please refer to the main project repository. Happy coding!