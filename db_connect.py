import mysql.connector
import pandas as pd

# Connect to MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="beam_failure_db"
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM beam_data")
data = cursor.fetchall()

columns = ['id', 'applied_load', 'span_length', 'material_strength', 'reinforcement_area', 'failure']
df = pd.DataFrame(data, columns=columns)

print(df.head())

cursor.close()
connection.close()
