class Cohort:
    def __init__(self,cohort_name,students):
        self.cohort_name = cohort_name
        self.students = students
    
    def student_summaries(self):
        return "\n".join([student.summary() for student in self.students])

    def class_list(self,class_name):
        student_list = []
        for student in self.students:
            if class_name in student.classes:
                student_list.append(student)
        return student_list