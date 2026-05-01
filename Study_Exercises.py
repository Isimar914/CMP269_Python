class LehmanCourse:
    def __init__(self, course_name, credits):
        self.course_name = course_name
        self.credits = credits
        self._student_count = 0

    def enroll_student(self):
        self._student_count += 1

    def display_info(self):
        print(f"Course: {self.course_name}, Credits: {self.credits}, Student Count: {self._student_count}")

class LabCourse(LehmanCourse):
    def __init__(self, course_name, credits, lab_fee):
        super().__init__(course_name, credits)
        self.lab_fee = lab_fee

    def display_info(self):
        print(f"Course: {self.course_name}, Credits: {self.credits}, Student Count: {self._student_count}, Lab Fee: ${self.lab_fee}")

class Professor:
    def get_role(self):
        return "Teaching and Research"

class Student:
    def get_role(self):
        return "Learning and Coding"

def print_role(person):
    print(person.get_role())

if __name__ == "__main__":
    course = LehmanCourse("CMP 269", 4)
    course.enroll_student()
    course.display_info()

    lab = LabCourse("CMP 269", 4, 100)
    lab.enroll_student()
    lab.display_info()

    professor = Professor()
    student = Student()

    print_role(professor)
    print_role(student)