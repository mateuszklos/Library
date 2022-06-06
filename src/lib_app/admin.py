from django.contrib import admin
from .models import Book, Author

# zarejestrowanie modeli dostępnych dla admina
admin.site.register(Book)
admin.site.register(Author)
