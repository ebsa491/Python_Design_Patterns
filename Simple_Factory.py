from abc import ABC, abstractmethod # ABCMeta, abstractmethod for python < 3.4

# Abstract class

class Book(ABC): # class Book(metaclass = ABCMeta): for python < 3.4 

    @abstractmethod
    def get_number_of_pages(self):
        pass


# Products

class CookingBook(Book):

    def get_number_of_pages(self):
        return 500

class ProgrammingBook(Book):

    def get_number_of_pages(self):
        return 300

# Factory

class PublicationFactory:
    
    def page_from_book_name(self, book_name):
        return eval(book_name)().get_number_of_pages()

# Client

if __name__ == '__main__':
    factory = PublicationFactory()

    input_book = input("Enter the book name> ")

    pages = factory.page_from_book_name(input_book)

    print(f"The book has {pages} pages.")