import json


def load_data():
    """ Функция чтения json-файла """
    try:
        with open("library.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data


def save_data(data):
    """ Функция записи json-файла """
    with open("library.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def app_command():
    """ Функция обработки команд пользователя"""
    user_command = input("Введите команду из списка: добавить, удалить, изменить статус, искать, показать все, выход ")
    if user_command == "добавить":
        add_book()
    elif user_command == "удалить":
        delete_book()
    elif user_command == "искать":
        search_book()
    elif user_command == "показать все":
        display_books()
    elif user_command == "изменить статус":
        status_books()
    elif user_command == "выход":
        finish_program()
    else:
        print("Введите корректное название команды из списка")
        app_command()


def add_book():
    """ Функция добавления книги """
    data = load_data()
    book = {
        "id": len(data) + 1,
        "title": input("Введите название книги: "),
        "author": input("Введите автора книги: "),
        "year": input("Введите год издания книги: "),
        "status": "в наличии"
    }
    data.append(book)
    save_data(data)
    print("Книга успешно добавлена!")
    app_command()


def delete_book():
    """ Функция удаления книги """
    data = load_data()
    book_id = int(input('Введите ID книги: '))
    for book in data:
        if book["id"] == book_id:
            data.remove(book)
            save_data(data)
            print("Книга успешно удалена!")
    else:
        print("Книга с указанным ID не найдена.")
    app_command()


def search_book():
    """ Функция поиска книги по title, author или year """
    data = load_data()
    user_search = input("Введите название книги, автора или год издания ").lower()
    for book in data:
        if book["title"].lower() == user_search:
            print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год издания: {book['year']}, "
                  f"Статус: {book['status']}")
            break
        elif book["author"].lower() == user_search:
            print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год издания: {book['year']}, "
                  f"Статус: {book['status']}")
            break
        elif book["year"].lower() == user_search:
            print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год издания: {book['year']}, "
                  f"Статус: {book['status']}")
            break
    else:
        print("Такая книга не найдена.")

    app_command()


def display_books():
    """ Функция отображения всех книг """
    data = load_data()
    for book in data:
        print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год издания: {book['year']}, "
              f"Статус: {book['status']}")
    app_command()


def status_books():
    """ Функция изменения статуса книги по ее ID """
    data = load_data()
    book_id = int(input('Введите ID книги: '))
    new_status = input("Введите новый статус 'в наличии' или 'выдана'")
    for book in data:
        if book["id"] == book_id:
            if book['status'] != new_status:
                book['status'] = new_status
                save_data(data)
                print(f"Статус книги успешно изменен на '{new_status}!'")
            else:
                print(f'Книга уже находится в статусе "{new_status}"')
    app_command()


def finish_program():
    """ Функция для выхода из программы """
    print("Вы вышли из программы, всего доброго!")
