from school_schedule.student import Student
from school_schedule.high_school_student import HighSchoolStudent
from school_schedule.middle_school_student import MiddleSchoolStudent

# first instance
quinn = MiddleSchoolStudent(
                "Claire", 
                "8th Grader", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ],
                True
            )

quinn.add_class("Painting")

# second instance
claire = HighSchoolStudent(
                "Claire", 
                "freshmen", 
                [
                    "Algebra", 
                    "Writing", 
                    "Contemporary Issues", 
                    "Gym", 
                    "Earth Science", 
                    "Painting"
                ],
                has_parking_privileges=True,
                clubs=["Algorithms Club"]
            )

students = [quinn, claire]
for student in students:
    print(student.summary())