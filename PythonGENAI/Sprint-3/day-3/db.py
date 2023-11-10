import mysql.connector

def create_connection():
    # Replace these values with your actual database credentials
    host = 'localhost'
    user = 'root'
    password = 'Kalyan@99'
    database = 'zomato'

    # Create a connection
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    if connection.is_connected():
        print("Connected to MySQL database")
    else:
        print("Connection failed")

    return connection
