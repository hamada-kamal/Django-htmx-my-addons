from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from booksApp.views import (
    create_book, 
    create_book_form, 
    detail_book, 
    update_book,
    delete_book,
    detail_author,
    update_author,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('htmx/book-form/', create_book_form,name="book-form"),
    path('htmx/book/<pk>/', detail_book, name="detail-book"),
    path('htmx/book/<pk>/update/', update_book, name="update-book"),
    path('htmx/book/<pk>/delete/', delete_book, name="delete-book"),
    path('htmx/author/<pk>/', detail_author, name="detail-author"),
    path('htmx/author/<pk>/update/', update_author, name="update-author"),
    path('<pk>/', create_book,name="create-book"),
    

]
