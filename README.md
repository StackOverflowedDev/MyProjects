# MyProjects: Drones Website
This repository contains my first **Django app**, a simple **drones website** built to showcase the basics of using Django for web development. The app allows users to view, add, and manage drone information.

---

## Project Overview
- Learn how to build a basic web application with **Django** and create a functional website to display and manage drone data.
- **Technologies Used**:
  - **Django**: Framework for building the web app.
  - **HTML**: Front-end structure.
  - **CSS**: Styling for the app.
  - **SQLite**: Django's default database for storing drone information.
  
---

## Features
- **View Drones**: Display a list of available drones.
- **Add Drones**: Users can add new drones to the list.
- **Manage Drones**: Basic features for managing drone information, like updating or deleting data.
- **User Authentication**: (Optional) Simple login system to restrict access to certain features.
- This project was built as part of the **CS50 Web Programming** course, where I learned how to use **Django** and other web development technologies.

---

## What I Learned
- How to **set up a Django project** and create views, models, and templates.
- How to **work with databases** in Django using SQLite.
- How to **implement forms** in Django to allow users to submit new data.
- **User authentication** (if implemented) to manage user sessions.

---
## License
This project is open-source and available under the MIT License.

---

## Project Structure
```
/MyProjects
│── /drones_app # Django app for managing drones
│ ├── models.py # Models for drone data
│ ├── views.py # Views for displaying drone information
│ ├── templates/ # HTML templates for the website
│ │ ├── drones_list.html # Template for listing drones
│ │ ├── add_drone.html # Template for adding a new drone
│ ├── urls.py # URL routing for the drones app
│── manage.py # Django manage script for running commands
│── /migrations # Database migrations
│── /static # Static files (CSS, images)
│── /templates # Base templates (if applicable)
│── README.md # This README file
```
## How to Run the Project

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/MyProjects.git
cd MyProjects
```
### 2. Install dependencies:
If you don't have Django installed, you can install it using pip:

```
pip install django
```
### 3. Run the Django development server:
```
python manage.py runserver
```
### 4. Access the app:
Open your browser and go to http://127.0.0.1:8000/ to view the drones website.

### 5. (Optional) Create migrations and apply them if you haven't already:
```
python manage.py makemigrations
python manage.py migrate
```

