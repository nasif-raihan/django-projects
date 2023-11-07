# Employee Management Website

## Introduction
This web application is designed to manage employee information efficiently. With this Employee Management Website, you can view all employee details, add new employees, remove existing employees, and search for employees using various filters. The application is built using Django, a high-level Python web framework, making it easy to use, secure, and customizable.

## Features

### 1. View Employee Details
- Access a comprehensive list of all employees registered in the system.
- View details such as employee ID, name, contact information, and other relevant data.

### 2. Add an Employee
- Add new employees to the database by providing necessary information.
- Include details such as employee name, contact number, address, role, and department.

### 3. Remove an Employee
- Remove employees from the database when they leave the organization or for any other reason.
- Ensure data integrity by securely deleting employee records.

### 4. Search an Employee by Filter
- Search for specific employees using filters such as name, employee ID, department, or role.
- Get instant results to quickly find the employee you are looking for.

## Prerequisites
- Python 3.10 installed on your system
- Django framework installed (`pip install django`)
- Docker installed on your system

## Getting Started
1. Clone the repository: 

`git clone https://github.com/nasif-raihan/django-projects.git`

2. Navigate to the project directory: 

`cd workforce_management`

3. Run migrations: 

`make migrations`

4. Create a superuser account:

`make superuser`

5. Start the development server: 

`make run-local`

or 

`make run-docker`

6. Access the admin panel at `http://localhost:8000/admin` to add employees using the superuser account.

## Usage
- Visit the homepage to view the list of employees and use the search functionality to find specific employees.
- Click on "Add Employee" to add a new employee to the database.
- Click on "Remove Employee" to remove an existing employee from the database.
- Click on "Filter Employee" to filter employees based on various criteria.

## Contributing
Contributions are welcome! If you want to contribute to this project, please follow these steps:
1. Fork the repository
2. Create a new branch: 

`git checkout -b feature/new-feature`

3. Make your changes and commit them: 

`git commit -m 'Add new feature'`

4. Push to the branch: 

`git push origin feature/new-feature`

5. Submit a pull request

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit/) - see the [LICENSE.md](https://opensource.org/license/mit/) file for details.

## Acknowledgments
- Thanks to the Django community for developing such a powerful and versatile web framework.
- Special thanks to the YouTube channel [NitManTalks](https://www.youtube.com/@NitManTalks).
