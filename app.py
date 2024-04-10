from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Replace these values with your MySQL database credentials
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'beyonce@1',
    'database': 'sqlflask',
}

@app.route('/')
def display_data():
    # Connect to the MySQL database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Execute a query to retrieve data
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()

    # Close the database connection
    cursor.close()
    connection.close()

    # Render the template and pass the data to it
    return render_template('display_data.html', data=data)

@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Connect to the MySQL database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Check if the name or email already exists in the database
        cursor.execute('SELECT * FROM users WHERE name = %s OR email = %s', (name, email))
        existing_user = cursor.fetchone()

        if existing_user:
            # Close the database connection
            cursor.close()
            connection.close()

            # Render the form template with an error message for duplicate entry
            return render_template('add_data.html', error_message="Name or Email already exists!")

        # Execute an INSERT query to add new data
        query = 'INSERT INTO users (name, email) VALUES (%s, %s)'
        values = (name, email)
        cursor.execute(query, values)

        # Commit the changes to the database
        connection.commit()

        # Close the database connection
        cursor.close()
        connection.close()

        # Print a debug message
        print("Data added successfully:", name, email)

        # Redirect to the display_data page after adding data
        return redirect(url_for('display_data'))

    # Render the form template for GET requests
    return render_template('add_data.html')


@app.route('/delete_data/<int:user_id>', methods=['POST'])
def delete_data(user_id):
    # Connect to the MySQL database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Execute a DELETE query to remove data
    query = 'DELETE FROM users WHERE id = %s'
    value = (user_id,)
    cursor.execute(query, value)

    # Commit the changes to the database
    connection.commit()

    # Close the database connection
    cursor.close()
    connection.close()

    # Redirect to the home page after deleting data
    return redirect(url_for('display_data'))

if __name__ == '__main__':
    app.run(debug=True) 


