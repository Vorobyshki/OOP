# Пользовательские исключения для проверок
class BookAlreadyIssuedError(Exception):
    """Книга уже выдана и не может быть выдана повторно."""
    pass

class BookNotIssuedError(Exception):
    """Книга уже доступна и не может быть возвращена."""
    pass

class Book:
    def __init__(self, isbn: str, author: str, title: str) -> None:
        # Защищенные атрибуты
        self._isbn: str = isbn
        self._author: str = author
        self._title: str = title
        self._is_available: bool = True

    # Чтобы снаружи нельзя было изменить
    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def author(self) -> str:
        return self._author

    @property
    def title(self) -> str:
        return self._title

    @property
    def is_available(self) -> bool:
        return self._is_available

    def issue(self) -> None:
        # Проверяем, можно ли выдать книгу
        if not self._is_available:
            raise BookAlreadyIssuedError("Книга уже выдана")
        self._is_available = False

    def return_book(self) -> None:
        # Проверяем, можно ли вернуть книгу
        if self._is_available:
            raise BookNotIssuedError("Книга уже доступна")
        self._is_available = True

# Ручная проверка в консоли
if __name__ == "__main__":
    book = Book("978-5-17", "Пушкин", "Евгений Онегин")
    print(book.is_available)
    
    book.issue()
    print(book.is_available)
    
    # Пытаемся выдать повторно
    try:
        book.issue()
    except BookAlreadyIssuedError as e:
        print("Ошибка:", e)
        
    # Пытаемся изменить название
    try:
        book.title = "Другое"
    except Exception:
        print("Метаданные изменить нельзя")