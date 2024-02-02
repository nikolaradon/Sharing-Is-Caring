# Sharing-Is-Caring
Project aims to create an interactive web platform that allows users to donate unnecessary items to trusted charitable institutions. This platform serves as a place where people can easily find ways to support those in need in their community through material donations.


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Introduction

The Sharing Is Caring project aims to create a digital platform that facilitates the donation process by allowing users to donate unwanted items to trusted charitable institutions. This README provides an overview of the project, its features, the technologies used, installation instructions, usage guidelines, and information on contributing to the project.

## Features

- **User Authentication:** Users can register, log in, and log out. Authentication is handled securely.

- **User Profiles:** Each user has a profile page.

- **Items Donation:** The platform allows users to contribute to charitable causes by donating various items. 


## Technologies

- **Django:** The web framework used for the backend.

- **HTML/CSS:** Frontend development for the user interface.

- **PostgreSQL:** Used for managing the project's database.
  
- **JavaScript:** Implements interactive features and behaviors on the client-side, such as form validation, dropdown selection, and form navigation.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.10
- Django 4.2
- Psycopg2-binary 2.9

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/nikolaradon/Sharings-Is-Caring.git
   cd Sharing-Is-Caring
   ```


2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

  
  - **On Windows:**
     ```
     .\venv\Scripts\activate
     ```

   - **On macOS/Linux:**
     ```
     source venv/bin/activate
     ```


3. **Apply Migrations:**
  ```bash
  python manage.py migrate
   ```


4. **Create a Superuser (Admin):**
  ```bash
  python manage.py createsuperuser
   ```

5. **Run the Development Server:**
  ```bash
  python manage.py runserver
   ```

**Access the Application:**
Open your web browser and go to http://127.0.0.1:8000/

**Access the Admin Panel:**
Visit http://127.0.0.1:8000/admin/ and log in with the superuser credentials.

## Usage
1. Register for an account.
2. Use the form to donate items
3. Select the items you wish to donate and proceed with the donation process.


## Contributing
If you would like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.
