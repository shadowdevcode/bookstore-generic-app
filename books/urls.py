from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path(r'', views.IndexView.as_view(), name='index'),
    path(r'<int:pk>/', views.DetailView.as_view(), name='detail'),
    path(r'add/', views.BookCreate.as_view(), name='book-add'),
    path(r'book/<int:pk>/', views.BookUpdate.as_view(), name='book-update'),
    path(r'<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
]
