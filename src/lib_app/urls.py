from django.urls import path

from . import views


urlpatterns = [
    path('', views.BooksView.as_view(), name='books'),
    path('search/', views.SearchResultsView.as_view(), name='search_results')
]