def sort_students(students):
  return sorted(students, key=lambda x: x.cgpa, reverse=True)


class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


students = [
    Student("John", "A001", 3.8),
    Student("Alice", "A002", 3.9),
    Student("Bob", "A003", 3.7)
]

sorted_students = sort_students(students)
for student in sorted_students:
  print(
      f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}"
  )
