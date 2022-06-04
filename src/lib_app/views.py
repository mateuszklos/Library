from django.views.generic import ListView
from django.db.models import Q
from .models import Book


# widok listy wszystkich książek
class BooksView(ListView):
    model = Book
    template_name = 'index.html'
    paginate_by = 8


# widok wyników wyszukiwania
class SearchResultsView(ListView):
    model = Book
    template_name = 'search_results.html'
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get('q')

        object_list = Book.objects.filter(
            Q(title__icontains=query)
        )
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
