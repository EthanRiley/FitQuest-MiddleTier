import csv
import mysql.connector

list_of_csv = ['Trainers.csv', 'Users.csv', 'TrainerHistory.csv', 'Foods.csv', 'Diet.csv', 'DietFoods.csv', 'Weight.csv', 'Equipment.csv', 'Staff.csv', 'WorkOrders.csv', 'UserRequests.csv', 'Programs.csv', 'Exercises.csv', 'UserExercises.csv', 'ProgramDetails.csv', 'UserPrograms.csv']

def insert_csv(filename, sqlconnection, schema):
    # Use schema
    print(filename)
    sqlconnection.database = schema

    # Read CSV
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        # Get table name and columnspip
        table_name = filename.split('.')[0]
        columns = next(csvreader)
        columns_string = ', '.join(columns)

        # Insert each row into the table
        for row in csvreader:
            values_string = ', '.join(['%s' for _ in row])
            query = f"INSERT INTO {table_name} ({columns_string}) VALUES ({values_string})"
            cursor = sqlconnection.cursor()
            cursor.execute(query, row)
            sqlconnection.commit()

if __name__ == "__main__":
    # Connect to MySQL server
    cnx = mysql.connector.connect(
        host='localhost',
        port=3200,
        user='root',
        password='abc123'
    )

    # Specify schema name
    schema = 'fitquest'

    # Insert data from CSV files
    for csv_file in list_of_csv:
        insert_csv(csv_file, cnx, schema)

    # Close the connection
    cnx.close()