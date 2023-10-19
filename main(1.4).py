import random
MIN_LEN_BOOK = 1
file_name = input("Введите название файла 'books.csv' или 'books-en.csv':")
if file_name != 'books-en.csv' and file_name != "books.csv":
    print("Неверно указано название файла")
list_books = []
with open(file_name) as csv_file:
    head = csv_file.readline()
    for s in csv_file:
        book = csv_file.readline()
        book = book.replace("\n", '')
        book = book.split(";")
        list_books.append(book)
    with open("test.txt", "w") as test_file:
        pass
        for book in range(20):
            rand_book = random.randint(1, len(list_books))
            if file_name == "books.csv":
                author = list_books[rand_book][4]
                title = list_books[rand_book][1]
                year = list_books[rand_book][6][6:10]
                test_file.write(f"{book+1}) Автор:{author}, Название:{title}, Год:{year}\n")
            elif file_name == "books-en.csv":
                author = list_books[rand_book][2]
                title = list_books[rand_book][1]
                year = list_books[rand_book][3]
                test_file.write(f"Автор:{author}, Название:{title}, Год:{year}\n")

print("Файл создан, см. test.txt")
