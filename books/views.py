from django.shortcuts import render
# Create your views here.
from bootstrap_modal_forms.generic import BSModalCreateView,\
    BSModalUpdateView, BSModalReadView, BSModalDeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from .forms import BookForm
from .models import Book


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'index.html'


class BookCreateView(BSModalCreateView):
    template_name = 'books/create_book.html'
    form_class = BookForm
    success_message = '새로운 데이터가 추가 되었습니다'
    success_url = reverse_lazy('books:index')


class BookUpdateView(BSModalUpdateView):
    model = Book
    template_name = 'books/update_book.html'
    form_class = BookForm
    success_message = '수정 완료 되었습니다'
    success_url = reverse_lazy('books:index')


class BookReadView(BSModalReadView):
    model = Book
    template_name = 'books/read_book.html'


class BookDeleteView(BSModalDeleteView):
    model = Book
    template_name = 'books/delete_book.html'
    success_message = '삭제 되었습니다'
    success_url = reverse_lazy('books:index')