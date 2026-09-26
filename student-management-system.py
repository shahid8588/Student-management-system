# ============================================
#   Student Management System
#   Author: Shahid Khan
#   Topics: OOP, File Handling, Exception Handling
# ============================================

import os

class Student:
    def __init__(self, name, roll_no, semester, gpa):
        self.name = name
        self.roll_no = roll_no
        self.semester = semester
        self.gpa = gpa

    def display(self):
        print(f"  Name      : {self.name}")
        print(f"  Roll No   : {self.roll_no}")
        print(f"  Semester  : {self.semester}")
        print(f"  GPA       : {self.gpa}")
        print(f"  Status    : {'Passing ✅' if self.gpa >= 2.0 else 'Failing ❌'}")
        print("-" * 35)

    def to_file_string(self):
        return f"{self.name},{self.roll_no},{self.semester},{self.gpa}\n"


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.filename = "students.txt"
        self.load_from_file()

    def load_from_file(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data) == 4:
                        student = Student(data[0], data[1], data[2], float(data[3]))
                        self.students.append(student)
        except FileNotFoundError:
            pass  # first time — file doesn't exist yet

    def save_to_file(self):
        with open(self.filename, "w") as file:
            for student in self.students:
                file.write(student.to_file_string())

    def add_student(self):
        print("\n--- Add New Student ---")
        try:
            name     = input("Enter name: ").strip().title()
            roll_no  = input("Enter roll number: ").strip()
            semester = input("Enter semester: ").strip()
            gpa      = float(input("Enter GPA (0.0 - 4.0): "))

            if gpa < 0.0 or gpa > 4.0:
                print("❌ Invalid GPA! Must be between 0.0 and 4.0")
                return

            student = Student(name, roll_no, semester, gpa)
            self.students.append(student)
            self.save_to_file()
            print(f"✅ Student '{name}' added successfully!")

        except ValueError:
            print("❌ Invalid input! GPA must be a number.")

    def display_all(self):
        if not self.students:
            print("❌ No students found!")
            return

        print("\n" + "=" * 35)
        print("       ALL STUDENTS")
        print("=" * 35)
        for i, student in enumerate(self.students, 1):
            print(f"Student {i}:")
            student.display()

    def search_student(self):
        print("\n--- Search Student ---")
        name = input("Enter student name to search: ").strip().title()

        found = False
        for student in self.students:
            if student.name == name:
                print(f"\n✅ Student Found!")
                student.display()
                found = True
                break

        if not found:
            print(f"❌ Student '{name}' not found!")

    def delete_student(self):
        print("\n--- Delete Student ---")
        roll_no = input("Enter roll number to delete: ").strip()

        for i, student in enumerate(self.students):
            if student.roll_no == roll_no:
                removed = self.students.pop(i)
                self.save_to_file()
                print(f"✅ Student '{removed.name}' deleted successfully!")
                return

        print(f"❌ Student with roll number '{roll_no}' not found!")

    def show_statistics(self):
        if not self.students:
            print("❌ No students to analyze!")
            return

        gpas = [s.gpa for s in self.students]
        passing = [s for s in self.students if s.gpa >= 2.0]
        failing = [s for s in self.students if s.gpa < 2.0]

        print("\n" + "=" * 35)
        print("       STATISTICS")
        print("=" * 35)
        print(f"Total Students  : {len(self.students)}")
        print(f"Passing         : {len(passing)}")
        print(f"Failing         : {len(failing)}")
        print(f"Highest GPA     : {max(gpas)}")
        print(f"Lowest GPA      : {min(gpas)}")
        print(f"Average GPA     : {sum(gpas)/len(gpas):.2f}")
        print("=" * 35)


def main():
    system = StudentManagementSystem()

    while True:
        print("\n" + "=" * 35)
        print("   STUDENT MANAGEMENT SYSTEM")
        print("=" * 35)
        print("  1. Add Student")
        print("  2. Display All Students")
        print("  3. Search Student")
        print("  4. Delete Student")
        print("  5. Show Statistics")
        print("  6. Exit")
        print("=" * 35)

        try:
            choice = int(input("Enter your choice (1-6): "))

            if choice == 1:
                system.add_student()
            elif choice == 2:
                system.display_all()
            elif choice == 3:
                system.search_student()
            elif choice == 4:
                system.delete_student()
            elif choice == 5:
                system.show_statistics()
            elif choice == 6:
                print("\n👋 Goodbye Shahid! Keep coding!")
                break
            else:
                print("❌ Invalid choice! Enter 1 to 6 only.")

        except ValueError:
            print("❌ Please enter a number!")


if __name__ == "__main__":
    main()
    