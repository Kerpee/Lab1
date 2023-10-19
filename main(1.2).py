MAX_LEN = 30
MIN_LEN_BOOK = 1
inf_file = input("Введите название файла 'books.csv' или 'books-en.csv':")
if inf_file != 'books-en.csv' and inf_file != "books.csv":
    print("Неверно указано название файла")
with open(inf_file) as csv_file:
    head = csv_file.readline()
    cnt_of_str = 0
    head = head.replace("\n", '')
    for s in csv_file:
        book = csv_file.readline()
        book = book.replace("\n", '')
        book = book.split(";")
        if (len(book) > MIN_LEN_BOOK) and (len(book[1])) >= MAX_LEN:
            cnt_of_str += 1
print(f"Количество книг с названием в более чем 30 символов:{cnt_of_str}")
