from classes.exe_1.book import Book
from classes.exe_1.save_file import SaveToFile
from classes.exe_2.Student import Student
from classes.exe_2.GradeCalculator import GradeCalculator
from classes.exe_3.Order import Order
from classes.exe_3.InvoicePrinter import InvoicePrinter


if __name__ == "__main__":
    book = Book("Harry Poter", "ari", "Harry poter is the best fantasy book")
    SaveToFile.save_to_file("date_2", book)

    student = Student("meir",[70,60,50])
    print(GradeCalculator.average_grade(student))

    order = Order(["cup", "bread","milk"],67.0)
    InvoicePrinter.print_invoice(order)
