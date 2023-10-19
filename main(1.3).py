MIN_LEN_BOOK = 1
YEAR = 2016
name_of_file = input("Введите название файла 'books.csv' или 'books-en.csv':")
if name_of_file != 'books-en.csv' and name_of_file != "books.csv":
    print("Неверно указано название файла")
with open(name_of_file) as csv_file:

    head = csv_file.readline()
    author = input("Введите имя и фамилию автора:")
    for s in csv_file:
        book = csv_file.readline()
        book = book.replace("\n", '')
        book = book.split(";")
        if name_of_file == 'books.csv':
            if len(book) > MIN_LEN_BOOK and ((author == book[3]) or (author == book[4])) and int(book[6][6:10]) < YEAR:
                print(book[1])
        elif len(book) > MIN_LEN_BOOK and name_of_file == "books-en.csv" and author == book[2]:
            print(book[1])
