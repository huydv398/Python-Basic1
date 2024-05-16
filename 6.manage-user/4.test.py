class Student:
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("Student added successfully.")

    def remove_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                print("Student removed successfully.")
                return
        print("Student not found.")

    def display_students(self):
        if len(self.students) == 0:
            print("No students found.")
            return
        print("List of students:")
        for student in self.students:
            print(f"Name: {student.name}, ID: {student.id}, Major: {student.major}")

# Example usage
manager = StudentManager()

student1 = Student("John Doe", "12345", "Computer Science")
student2 = Student("Jane Smith", "67890", "Mathematics")

manager.add_student(student1)
manager.add_student(student2)
manager.display_students()

manager.remove_student("12345")
manager.display_students()