# ============================================
# 📚 Concept: Class Methods
# ============================================
# Class methods are methods that belong to the class and not to the instance of the class.
# - They take the class (`cls`) as the first argument instead of the instance (`self`).
# - Class methods are used to modify class-level variables and to define actions 
#   that are related to the class, not to a particular object.

class Book:
    # Class variable that is shared by all instances of the class
    total_books = 0  # This variable tracks the total number of books created

    def __init__(self, title, author):
        # Instance variables initialized with constructor
        self.title = title
        self.author = author
        # Every time a new Book object is created, increment the total_books count
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        # Accesses the class-level variable total_books and increments it
        cls.total_books += 1
        # Prints the updated count of books every time a new one is added
        print(f"Total books: {cls.total_books}")

# Usage
book1 = Book("1984", "George Orwell")
# When this book is created, the class method increment_book_count is called
book2 = Book("To Kill a Mockingbird", "Harper Lee")
# The count of total_books is updated again

# ============================================
# 📝 Assignment:
# - Create a class `Book` with a class variable `total_books` that keeps track of the number of books created.
# - Add a class method `increment_book_count()` to increase the `total_books` count when a new book is added.
# - Notice how `increment_book_count()` works with the class-level variable and not instance-specific data.
# ============================================
 
