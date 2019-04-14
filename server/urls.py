# server URL Configuration
from django.contrib import admin
from django.urls import path, include
from .views import CustomLoginView, SignUpView, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', logout_view, name='logout'),
    path('login/',  CustomLoginView.as_view(), name='login'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path("", include('books.urls', namespace='books'))
]