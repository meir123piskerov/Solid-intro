from classes.exe_2.Student import Student
class GradeCalculator(Student):
    @staticmethod
    def average_grade(Calculator:Student):
        avg1 = sum(Calculator.grades) / len(Calculator.grades)
        return avg1
