# OctoFit Tracker

## Overview

The OctoFit Tracker is a fitness application designed to help users track their activities, manage teams, and receive personalized workout suggestions. The application includes features such as user authentication, activity logging, competitive leaderboards, and more.

## Project Structure

The project is organized into two main directories: `backend` and `frontend`.

### Backend

- **venv/**: Contains the Python virtual environment for isolating project dependencies.
- **requirements.txt**: Lists the required Python packages for the project.
- **octofit_tracker/**: The main Django application directory.
  - **manage.py**: Command-line utility for interacting with the Django project.
  - **octofit_tracker/**: Contains the core Django application files.
    - **\_\_init\_\_.py**: Marks the directory as a Python package.
    - **settings.py**: Configuration settings for the Django project.
    - **urls.py**: URL routing for the application.
    - **asgi.py**: Entry point for ASGI-compatible web servers.
    - **wsgi.py**: Entry point for WSGI-compatible web servers.
- **README.md**: Documentation and instructions related to the backend.

### Frontend

- **README.md**: Documentation and instructions related to the frontend.
- **(frontend-src-placeholder)**: Placeholder for the frontend source code.

### Development

- **.vscode/launch.json**: Configuration settings for launching the Django application in a development environment.

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd octofit-tracker
   ```

2. **Set up the Python virtual environment**:
   ```bash
   python3 -m venv backend/venv
   source backend/venv/bin/activate
   ```

3. **Install the required packages**:
   ```bash
   pip install -r backend/requirements.txt
   ```

4. **Run the Django application**:
   Use the launch configuration in `.vscode/launch.json` to start the application.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for details.