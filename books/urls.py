from django.urls import path
from .views import BookListView, BookCreateView,\
    BookReadView, BookUpdateView, BookDeleteView
    
app_name = 'books'
urlpatterns = [
    path('', BookListView.as_view(), name='index'),
    path('create/', BookCreateView.as_view(), name='create'),
    path('read/<int:pk>', BookReadView.as_view(), name='read'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='delete'),
]
