class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_students:
                lecturer.grades_students[course] += [grade]
            else:
                lecturer.grades_students[course] = [grade]
        else:
            return 'Ошибка'

    def all_grades_rev(self):
        sum_grades = []
        for grades in self.grades.values():
            for grade in grades:
                sum_grades += [grade]
        return sum_grades

    def average_gr(self):
        average_grade = sum(self.all_grades_rev()) / len(self.all_grades_rev())
        return round(average_grade,1)

    def __eq__(self, other):
        return self.average_gr() == other.average_gr()

    def __ne__(self, other):
        return self.average_gr() != other.average_gr()

    def __lt__(self, other):
        return self.average_gr() < other.average_gr()

    def __gt__(self, other):
        return self.average_gr() > other.average_gr()

    def __le__(self, other):
        return self.average_gr() <= other.average_gr()

    def __ge__(self, other):
        return self.average_gr() >= other.average_gr()

    def __str__(self):
        return (f'Имя: {self.name} \nФамилия: {self.surname} '
            f'\nСредняя оценка за домашние задания: {self.average_gr()} '
            f'\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} '
            f'\nЗавершенные курсы: {', '.join(self.finished_courses)}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_students = {}

    def all_grades_st(self):
        sum_grades = []
        for grades in self.grades_students.values():
            for grade in grades:
                sum_grades += [grade]
        return sum_grades

    def average(self):
        average_grades = sum(self.all_grades_st()) / len(self.all_grades_st())
        return round(average_grades,1)

    def __eq__(self, other):
        return self.average() == other.average()

    def __ne__(self, other):
        return self.average() != other.average()

    def __lt__(self, other):
        return self.average() < other.average()

    def __gt__(self, other):
        return self.average() > other.average()

    def __le__(self, other):
        return self.average() <= other.average()

    def __ge__(self, other):
        return self.average() >= other.average()

    def __str__(self):
        return (f'Имя: {self.name} '
                f'\nФамилия: {self.surname} '
                f'\nСредняя оценка за лекции: {self.average()}')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


student_1 = Student('Ваня', 'Ванин', 'мужской')
student_1.courses_in_progress = ['Python', 'Java']
student_1.finished_courses = ['C#']

student_2 = Student('Дима', 'Димин', 'мужской')
student_2.courses_in_progress = ['Python', 'C#']
student_2.finished_courses = ['Основы программирования']

student_3 = Student('Фрося', 'Фросина', 'женский')
student_3.courses_in_progress = ['Java', 'C#']
student_3.finished_courses = ['Основы программирования']

lecturer_1 = Lecturer('Ирина', 'Иринова')
lecturer_1.courses_attached = ['Python']

lecturer_2 = Lecturer('Света', 'Светина')
lecturer_2.courses_attached = ['C#']

lecturer_3 = Lecturer('Пётр', 'Петров')
lecturer_3.courses_attached = ['Java']

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_3,'Java', 9)
student_2.rate_lecturer(lecturer_1, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'C#', 8)
student_3.rate_lecturer(lecturer_3,'Java', 9)
student_3.rate_lecturer(lecturer_2, 'C#', 10)

reviewer_1 = Reviewer('Иван', 'Иванов')
reviewer_1.courses_attached = ['Python']
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Python', 8)

reviewer_2 = Reviewer('Арнольд', 'Арнольдович')
reviewer_2.courses_attached = ['C#', 'Python']
reviewer_2.rate_hw(student_2, 'C#', 9)
reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 8)

reviewer_3 = Reviewer('Даня', 'Данин')
reviewer_3.courses_attached = ['Java']
reviewer_3.rate_hw(student_1, 'Java', 10)
reviewer_3.rate_hw(student_3, 'Java', 9)

students = [student_1, student_2, student_3]
lecturers = [lecturer_1, lecturer_2, lecturer_3]

def average_all_students_grades(students, course):
    all_students_grades = []
    for student in students:
        all_students_grades.extend(student.grades.get(course, []))
    return sum(all_students_grades) / len(all_students_grades)

def average_all_lecturers_grades(lecturers, course):
    all_lecturers_grades = []
    for lecturer in lecturers:
        all_lecturers_grades.extend(lecturer.grades_students.get(course,[]))
    return sum(all_lecturers_grades) / len(all_lecturers_grades)


print(reviewer_1)
print(reviewer_2)
print(reviewer_3)

print(lecturer_1)
print(lecturer_2)
print(lecturer_3)

print(student_1)
print(student_2)
print(student_3)

print(lecturer_3 == lecturer_2)
print(lecturer_1 != lecturer_2)
print(lecturer_2 < lecturer_3)
print(lecturer_1 > lecturer_2)
print(lecturer_3 <= lecturer_1)
print(lecturer_2 >= lecturer_1)

print(student_1 == student_2)
print(student_3 != student_2)
print(student_1 < student_3)
print(student_2 > student_1)
print(student_3 <= student_1)
print(student_2 >= student_1)

print(average_all_students_grades(students, 'Java'))
print(average_all_lecturers_grades(lecturers, 'C#'))
