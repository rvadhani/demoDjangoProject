from django.test import TestCase

# Create your tests here.


from library.models import Book
from django.db import connection
books = Book.objects.all()
# books = Book.objects.select_related('authors')

for book in books:
    print(book.authors.name)

print(len(connection.queries))

