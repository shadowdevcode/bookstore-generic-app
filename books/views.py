from django.views import generic
from .models import Book
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView


class IndexView(generic.ListView):
    template_name = 'books/index.html'

    ''' get_queryset: Get the list of items for this view '''
    def get_queryset(self):
        return Book.objects.all()


class BookCreate(CreateView):
    model = Book
    fields = ['name', 'author', 'price', 'type', 'book_image']


class BookUpdate(UpdateView):
    model = Book
    fields = ['name', 'author', 'price', 'type', 'book_image']


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books:index')


class DetailView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'
