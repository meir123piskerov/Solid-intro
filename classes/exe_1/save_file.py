from classes.exe_1.book import Book


class SaveToFile:
    @staticmethod
    def save_to_file(file_name: str, book: Book):
        with open(f"{file_name}.txt", "a") as f:
            f.write(book.content)
