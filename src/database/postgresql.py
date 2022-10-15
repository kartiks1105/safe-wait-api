import psycopg2
from database.tables.driver_information import DriverInformation

from database.tables.student_information import StudentInformation

class PostgreSQL:

    def __init__(self):
        self.connection = psycopg2.connect(
            database="SafeWait",
            host="localhost",
            user="postgres",
            password="root",
            port="5432"
        )
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()
    
    def get_student_information(self, student_id):
        query = '''
            SELECT * FROM student_information
            WHERE student_id = %s
        '''
        self.cursor.execute(query, [student_id])
        row = self.cursor.fetchone()
        return StudentInformation(row) if row else None
    
    def get_driver_information(self, student_id):
        query = '''
            SELECT * FROM driver_information
            WHERE student_id = %s
        '''
        self.cursor.execute(query, [student_id])
        row = self.cursor.fetchone()
        return DriverInformation(row) if row else None