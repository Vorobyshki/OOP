from library_system import Library, BookNotFoundError
from book import Book, BookAlreadyIssuedError, BookNotIssuedError


def main():
    # Создаем библиотеку
    lib = Library()

    # Создаем две книги
    b1 = Book("978-5-17-113589-6", "Мастер и Маргарита", "Булгаков")
    b2 = Book("978-2-07-061124-6", "Маленький принц", "Экзюпери")

    # Добавляем их в библиотеку
    lib.add_book(b1)
    lib.add_book(b2)

    print("Все книги:", lib.list_all_books())
    print("Доступные:", lib.list_available_books())
    print("Выданные:", lib.list_checked_out_books())

    print("\n--- Выдаем книгу ---")
    lib.checkout_book(b1.isbn)
    print("Доступные:", lib.list_available_books())
    print("Выданные:", lib.list_checked_out_books())

    print("\n--- Пытаемся выдать повторно ---")
    try:
        lib.checkout_book(b1.isbn)
    except BookAlreadyIssuedError as e:
        print("Ошибка:", e)

    print("\n--- Возвращаем книгу ---")
    lib.return_book(b1.isbn)
    print("Доступные:", lib.list_available_books())

    print("\n--- Пытаемся вернуть повторно ---")
    try:
        lib.return_book(b1.isbn)
    except BookNotIssuedError as e:
        print("Ошибка:", e)
        
    print("\n--- Ищем несуществующую книгу ---")
    try:
        lib.checkout_book("000-000")
    except BookNotFoundError as e:
        print("Ошибка:", e)


if __name__ == "__main__":
    main()