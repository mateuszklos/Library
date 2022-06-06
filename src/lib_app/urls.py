from django.urls import path

from . import views

urlpatterns = [
    path('', views.BooksView.as_view(), name='books'),
    path('search', views.SearchResultsView.as_view(), name='search_results'),
    path('register', views.register_request, name="register"),
    path('login', views.login_request, name='ilogin'),
    path('logout', views.logout_request, name='ilogout'),
    path('add/<int:id>', views.addtolist, name='addtolist'),
    path('remove/<int:id>', views.removefromlist, name='removefromlist'),
    path('myListView', views.myListView.as_view(), name='mylist'),
]
