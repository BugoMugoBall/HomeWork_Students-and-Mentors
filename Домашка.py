from functools import total_ordering


@total_ordering
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.lecturer_gradee = {}

    def average_grade(self):
        if not self.grades:
            return 0
        total_grades = 0
        count = 0
        for course_grade in self.grades.values():
            total_grades += sum(course_grade)
            count += len(course_grade)
        return total_grades / count


    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.average_grade():.1f}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: Введение в программирование"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return "Ошибка сравнения"
        return self.average_grade() == other.average_grade()

    def __lt__(self, other):
        if not isinstance(other, Student):
            return "Ошибка сравнения"
        return self.average_grade() < other.average_grade()


    def lecture_grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}"



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            return 0
        total_grades = 0
        count = 0
        for course_grade in self.grades.values():
            total_grades += sum(course_grade)
            count += len(course_grade)
        return total_grades / count

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {self.average_grade():.1f}"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if not (0 <= grade <= 10):
                return "оценка должна быть от 0 до 10"
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            return None
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}"


def average_grade_of_student(students, course):
    total_grade = 0
    count = 0
    for student in students:
        if course in student.grades:
            total_grade += sum(student.grades[course])
            count += len(student.grades[course])
    if count:
        return total_grade / count
    else:
        return 0

def average_grade_of_lecturer(lecturers, course):
    total_grade = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grade += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    if count:
        return total_grade / count
    else:
        return 0



student_1 = Student("Иван","Кузьмин", "М" )
student_2 = Student("Регина", "Кузьмина", "Ж")


lecturer_1 = Lecturer("Евгений", "Угадайков" )
lecturer_2 = Lecturer("Василий", "Незнайков")


reviewer_1 = Reviewer("Алена", "Всемпетерковна")
reviewer_2 = Reviewer("Данил", "Всемколович")



student_1.courses_in_progress += ["Python", "Git"]
student_1.finished_courses += ["Введение в программирование"]
student_2.courses_in_progress += ["Python", "Java"]

lecturer_1.courses_attached += ["Python", "Git"]
lecturer_2.courses_attached += ["Java"]


reviewer_1.courses_attached += ["Python", "Git"]
reviewer_2.courses_attached += ["Java"]


reviewer_1.rate_hw(student_1, "Python", 9)
reviewer_1.rate_hw(student_1, "Python", 10)
reviewer_2.rate_hw(student_2, "Java", 8)
student_1.lecture_grade(lecturer_1, "Python", 10)
student_2.lecture_grade(lecturer_2, "Java", 9)


print(student_1)
print(student_2)
print(lecturer_1)
print(reviewer_1)


print(student_2 < student_1)
print(lecturer_1 == lecturer_2)


students_list = [student_1, student_2]
lecturers_list = [lecturer_1, lecturer_2]

print(f"Средняя оценка за домашние задания по Python: {average_grade_of_student(students_list, 'Python'):.1f}")
print(f"Средняя оценка за лекции по Python: {average_grade_of_lecturer(lecturers_list, 'Python'):.1f}")
print(f"Средняя оценка за домашние задания по Java: {average_grade_of_student(students_list, 'Java'):.1f}")
print(f"Средняя оценка за лекции по Java: {average_grade_of_lecturer(lecturers_list, 'Java'):.1f}")


