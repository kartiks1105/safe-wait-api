class StudentInformation:

    def __init__(self, database_row):
        self.student_id = database_row[0]
        self.first_name = database_row[1]
        self.middle_name = database_row[2]
        self.last_name = database_row[3]
        self.address = database_row[4]
        self.postal_code = database_row[5]