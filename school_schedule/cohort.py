# Write cohort class here
# Write a class_list function which takes a class name as a parameter and returns all the students in that class
# Write code in main.py to try the functions out

class Cohort:
    def __init__(self, cohort_name, students):
        self.name = cohort_name
        self.students = list(students) # lets us reduce side effects by  making a copy

    def student_summaries(self):
        summaries = []
        for student in self.students:
            summaries.append(student.summary())

        return "\n".join(summaries)

    def class_list(self, class_name):
        student_in_class = []
        for student in self.students:
            if class_name in student.classes:
                student_in_class.append(student.name)
        
        return "\n".join(student_in_class)