# SQLFlask CRUD Application

SQLFlask CRUD Application is a simple web application built with Flask and MySQL that allows users to perform CRUD (Create, Read, Update, Delete) operations on a database of users.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features) -[Working]

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your_username/sqlflask-crud.git
   ```

2. Navigate to the project directory:

   ```bash
   cd sqlflask-crud
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Import the `database.sql` file into your MySQL database to create the necessary database and table structure.

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000/` to access the application.

3. You can perform the following actions:

   - View the list of users.
   - Add a new user.
   - Delete an existing user.

## Features

- Display a list of users from the MySQL database.
- Add new users with unique names and email addresses.
- Delete users from the database.

WORKING;
Sure, let's break down how the SQLFlask CRUD application works:

### Database Setup

1. **Database Creation**: The application begins by ensuring that the `sqlflask` database exists. If it doesn't exist, it creates it using `CREATE DATABASE IF NOT EXISTS sqlflask;`.

2. **Database Selection**: After ensuring the database exists, it selects the `sqlflask` database using `USE sqlflask;`.

3. **Table Creation**: Next, it creates a table named `users` if it doesn't already exist. This table contains columns for `id` (primary key), `name`, and `email`.

### Flask Application

1. **Flask Setup**: The Flask application is initialized, and the necessary modules and packages are imported.

2. **Database Configuration**: The application specifies the database configuration, including the host, username, password, and database name.

3. **Route Definitions**:

   - **Display Data Route (`/`)**: When a user navigates to the root URL, the application retrieves all user data from the `users` table and renders the `display_data.html` template with the data.

   - **Add Data Route (`/add_data`)**: This route handles both GET and POST requests.

     - For GET requests, it renders the `add_data.html` template, allowing users to input new user data.
     - For POST requests, it receives form data submitted by users, validates it, adds the new user to the database if it's valid, and redirects to the display page.

   - **Delete Data Route (`/delete_data/<int:user_id>`)**: This route handles POST requests to delete user data. It receives the user ID as a parameter, deletes the corresponding user from the database, and redirects to the display page.

4. **Templates**: The application uses HTML templates for rendering pages to users. These templates include:

   - `display_data.html`: Displays the list of users fetched from the database.
   - `add_data.html`: Provides a form for users to add new user data.

5. **Static Files**: The application serves static files (CSS and JavaScript) to enhance the user interface and functionality.

### Frontend Interaction

1. **Adding Data**: Users can add new user data by filling out the form on the `/add_data` route. Upon submission, the form data is sent to the server, validated, and added to the database if valid.

2. **Displaying Data**: The application retrieves user data from the database and displays it on the homepage (`/`). Users can see the list of users along with options to delete individual users.

3. **Deleting Data**: Users can delete user data by clicking the "Delete" button next to each user. This triggers a POST request to the `/delete_data` route, which deletes the corresponding user from the database and updates the displayed list of users.

### Backend Logic

1. **Database Interaction**: The application connects to the MySQL database using the specified database configuration. It executes SQL queries to perform CRUD operations on the `users` table.

2. **Error Handling**: The application handles errors such as duplicate entries and database connection issues and provides appropriate feedback to users.

3. **Debugging**: Debugging messages are printed to the console to assist in troubleshooting and monitoring application behavior.
