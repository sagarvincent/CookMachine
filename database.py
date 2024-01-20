import mysql.connector


class db_handler():

    def __init__(self, host, user,password, database):

        self.connection = mysql.connector.connect(host=host,user=user,password=password, database=database)
        self.cursor = self.connnection.cursor()
        self.create_table()

    def create_table(self):
        # Define your table creation SQL statements
        create_table_sql = '''
            CREATE TABLE IF NOT EXISTS my_table (
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
            );
        '''
        self.cursor.execute(create_table_sql)
        self.connection.commit()

    def insert_data(self, name, age):
        # Insert data into the table
        insert_data_sql = '''
            INSERT INTO my_table (name, age) VALUES (?, ?);
        '''
        self.cursor.execute(insert_data_sql, (name, age))
        self.connection.commit()

    def fetch_data(self):
        # Fetch and print data from the table
        fetch_data_sql = '''
            SELECT * FROM my_table;
        '''
        self.cursor.execute(fetch_data_sql)
        data = self.cursor.fetchall()
        for row in data:
            print(row)

    def close_connection(self):
        # Close the database connection
        self.connection.close()













