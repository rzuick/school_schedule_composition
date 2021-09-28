from .student import Student

class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, gets_transportation=False):
        super().__init__(name, grade, classes)
        self.gets_transportation = gets_transportation

    def summary(self):
        student_summary = super().summary()
        transportation_messge = self.display_transportation_message()

        return "\n".join((student_summary, transportation_messge))

    def display_transportation_message(self):
        if self.gets_transportation:
            return f"{self.name} takes the bus"
        else:
            return f"{self.name} walks or is a car rider"