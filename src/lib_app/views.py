from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.db.models import Q
from .models import Book, Author
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# widok listy wszystkich książek
class BooksView(ListView):
    model = Book
    template_name = 'index.html'
    paginate_by = 8


# widok wyszukiwania
class SearchResultsView(ListView):
    model = [Book, Author]
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


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("books")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('books')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('books')


@login_required
def addtolist(request, id):
    book = get_object_or_404(Book, pk=id)

    if request.method == 'POST':
        book = Book.objects.get(id=id)
        book.user = request.user
        book.is_in_list = True
        book.save()
        messages.success(request, 'added!')

        return redirect('books')

    return render(request, 'add.html', {'book': book})


@login_required
def removefromlist(request, id):
    book = get_object_or_404(Book, pk=id)

    if request.method == 'POST':
        book = Book.objects.get(id=id)
        book.is_in_list = False
        book.save()
        messages.success(request, 'removed!')

        return redirect('mylist')

    return render(request, 'remove.html', {'book': book})


class myListView(ListView):
    model = Book
    template_name = 'my_list.html'
    paginate_by = 8

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).filter(is_in_list=True)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(myListView, self).dispatch(*args, **kwargs)
