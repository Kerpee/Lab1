with open("books.csv") as csv_file:
    num_of_cnt = 0
    for s in csv_file:
        num_of_cnt += 1
    print(f"Количество записей:{num_of_cnt}")
