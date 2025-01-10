import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    auth_plugin="mysql_native_password",
    database = "schooldb"
)