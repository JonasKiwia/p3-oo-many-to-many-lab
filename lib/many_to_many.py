class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("name must be a string")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        """Return a list of contracts for this author."""
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        """Return a list of books associated with this author via contracts."""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Sign a contract between this author and the given book."""
        # Validate the book type.
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Return the sum of royalties percentages from all of this author's contracts."""
        return sum(contract.royalties for contract in self.contracts())



class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("title must be a string")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        # Retrieve authors from this book's contracts, ensuring uniqueness.
        unique_authors = []
        for contract in self.contracts():
            if contract.author not in unique_authors:
                unique_authors.append(contract.author)
        return unique_authors



class Contract:
    all = []

    def __init__(self, author, book, date, royalties):

        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        if not isinstance(date, str):
            raise Exception("date must be a string")
        return [contract for contract in cls.all if contract.date == date]
