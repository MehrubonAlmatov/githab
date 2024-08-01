class Books:
    def __init__(self, book_name, book_author, book_type):
        self.book_name = book_name
        self.book_author = book_author
        self.book_type = book_type

    def __str__(self):
        return f"{self.book_name} kitobi muallifi {self.book_author}, kitob {self.book_type} kitoblar toifasiga kiradi"

    def name(self, new_name):
        print(f"Kitob nomi {self.book_name}dan {new_name}ga o'zgartirildi")
        self.book_name = new_name

    def author(self, new_author):
        print(f"Kitob muallifi {self.book_author}dan {new_author}ga o'zgartirildi")
        self.book_author = new_author

book1 = Books("Otamdan qolgan dalalar", "Tog'ay Murod", "tarixiy")
book2 = Books("Kichik prince", "Antoine de Saint-Exupery", "badiiy")
book3 = Books("Dasturlash asoslari", "John Doe", "ta'lim")

print(book1)
print(book2)
print(book3)

book1.name("Otamdan qolgan dalalar (yangilangan)")
book1.author("Tog'ay Murod (yangilangan)")

print(book1)
