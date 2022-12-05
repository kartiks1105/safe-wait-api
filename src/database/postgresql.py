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
    
    def get_student_information(self, student_id, password):
        query = '''
            SELECT * FROM student_information
            WHERE student_id = %s
            AND password = %s
        '''
        self.cursor.execute(query, [student_id, password])
        row = self.cursor.fetchone()
        return StudentInformation(row) if row else None
    
    def get_driver_information(self, student_id, password):
        query = '''
            SELECT * FROM driver_information
            WHERE student_id = %s
            AND password = %s
        '''
        self.cursor.execute(query, [student_id, password])
        row = self.cursor.fetchone()
        return DriverInformation(row) if row else None

    def verifyStudent(self, student_id, password):
        query = """
            SELECT * FROM public.accounts
            WHERE student_id = %s
            AND password = %s
        """
        self.cursor.execute(query, [student_id, password])
        row = self.cursor.fetchone()
        if row:
            account_data = {
                'student_id': row[0],
                'first_name': row[1],
                'middle_name': row[2],
                'last_name': row[3],
                'address': row[4],
                'postal_code': row[5],
                'password': row[6],
                'profile_type': row[7]
            }
            return account_data
        else:
            return {}