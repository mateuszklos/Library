from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Book


def index(request):
    return render(request, 'index.html')


class BooksView(ListView):
    model = Book
