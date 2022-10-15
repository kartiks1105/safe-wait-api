from database.tables.student_information import StudentInformation


class DriverInformation(StudentInformation):

    def __init__(self, database_row):
        super().__init__(database_row)