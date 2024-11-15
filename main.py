class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'   
    def __eq__(self, other_student):
        return (self.average_grade() == other_student.average_grade())
    
    def average_grade(self):
        total_grades = 0
        total_count = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            total_count += len(grades)

        if total_count > 0:
            average_grade = total_grades / total_count
        else:
            average_grade = 0
        return average_grade
    
    def __str__(self):
        in_progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n'
        f'Средняя оценка за домашние задания: {self.average_grade()}\n'
        f'Курсы в процессе изучения: {in_progress}\n'
        f'Завершенные курсы: {finished}')
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        total_grades = 0
        total_count = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            total_count += len(grades)

        if total_count > 0:
            average_grade = total_grades / total_count
        else:
            average_grade = 0
        return average_grade
    
    def __str__(self):
        return (f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n'
        f'Средняя оценка за лекции {self.average_grade()}')
    
    def __eq__(self, other_lecturer):
        return (self.average_grade() == other_lecturer.average_grade())

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return (f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}')



 
student1 = Student('Макар', 'Сергеев', 'мужской')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Git']
student1.grades = {'Python': [5, 5, 10], 'Git': [8, 8]}

student2 = Student('Ирина', 'Иванова', 'женский')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Git']
student2.grades = {'Python': [10, 5, 8], 'Git': [8, 9]}

lecturer1 = Lecturer('Артем', 'Смирнов')
lecturer1.courses_attached += ['Python']
lecturer1.grades = {'Python': [9, 10, 8]}

lecturer2 = Lecturer('Павел', 'Сидоров')
lecturer2.courses_attached += ['Python']
lecturer2.grades = {'Python': [6, 8, 7]}

reviewer1 = Reviewer('Василий', 'Игнатов')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Альбина', 'Валиулина')
reviewer2.courses_attached += ['Python']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Python', 10)

def average_student_grade(students, course):
    total_grades = 0
    total_count = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            total_count += len(student.grades[course])
    if total_count > 0:
        return total_grades / total_count
    return 0

def average_lecturer_grade(lecturers, course):
    total_grades = 0
    total_count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            total_count += len(lecturer.grades[course])
    if total_count > 0:
        return total_grades / total_count
    return 0

students = [student1, student2]

lecturers = [lecturer1, lecturer2]

course_name = 'Python'
avg_student_grade = average_student_grade(students, course_name)
avg_lecturer_grade = average_lecturer_grade(lecturers, course_name)

print(f'Средний балл за домашние задания по курсу {course_name}: {avg_student_grade}')
print(f'Средний балл за лекции по курсу {course_name}: {avg_lecturer_grade}')

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)