fi=input("Введите название файла 'books.csv' или 'books-en.csv':")
if fi!='books-en.csv' and fi!="books.csv":
    print("Неверно указано название файла")
f=open(fi)
head=f.readline()#Считываем заголовок
a=[]#Вводим список для информации про книги
spisok=[]
for s in f:#Проходим по файлу
    i=f.readline()#Считываем информацию про книги
    i=i.split("\n")#Разделяем информацию по строчкам
    a.append(i)#Добавляем все книги в список
for i in range(len(a)-1):# Проходим по списку книг, не считая последний элемент,т.к. он пустой
    q=a[i][0].split(";")#Разделяем информацию про книгу на отдельные элементы
    spisok.append(q)#Добавляем информацию про книгу в список
vvod=input("Введите фамилию автора:")#Получаем фамилию автора для поиска
for i in range(len(spisok)):#Проходим по списку книг
    if fi=='books.csv':
        if (vvod in spisok[i][3]) or (vvod in spisok[i][4]) and int(spisok[i][6][6:10])<2016:
            print(spisok[i][1])
    else:
        print(spisok)
        if int(spisok[i][3])<2016 and vvod in spisok[i][2]:
            print(spisok[i][1])