from collections import namedtuple

Book = namedtuple("anything", "title author genre") # Альтернатива ["tutle", "author", "genre"]
b1 = Book("Солярис", "Станислав Лем", "научная фантастика")
b2 = Book("Три мушкетёра", "Александр Дюма", "приключенческий роман")
b3 = Book("1984", "Джордж Оруэлл", "антиутопия")

print(b1)
print(b2.title, b2.author, b2.genre, sep=" | ")
print(b3.author)
print(type(b3)) # интересно что тип мы указываем самостоятельно, и type(b3) != namedtuple
