from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404, redirect, render
from .forms import BookFormSet, BookForm, AuthorForm
from .models import Author, Book

def create_book(request, pk):
    author = Author.objects.get(id=pk)
    books = Book.objects.filter(author=author)
    form = BookForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return redirect("detail-book", pk=book.id)
        else:
            return render(request, "partials/book_form.html", {
                "form":form,
            })
          

    context = {
        "form": form,
        "author": author,
        "books": books,
        
    }

    return render(request, "create_book.html", context)


def create_book_form(request):
    context = {
        "form": BookForm()
    }
    return render(request, 'partials/book_form.html', context)


def detail_book(request,pk):
    book = Book.objects.get(pk=pk)
    context = {
        "book": book,
    }
    return render(request, 'partials/book_detail.html', context)


def update_book(request,pk):
    book = Book.objects.get(pk=pk)
    form = BookForm(request.POST or None,instance=book)
    if request.method=="POST":
        if form.is_valid():
            book = form.save()
            return redirect("detail-book", pk=book.id)
        context = {
            "form": form,
            "book": book,
        }
    return render(request, 'partials/book_form.html', context)



def delete_book(request,pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return HttpResponse('')


def detail_author(request,pk):
    author = Author.objects.get(pk=pk)
    books = Book.objects.filter(author=author)
    context = {
        "author": author,
        "books": books,
    }
    return render(request, 'partials/author_detail.html', context)


def update_author(request,pk):
    author = Author.objects.get(pk=pk)
    books = Book.objects.filter(author=author)
    form = AuthorForm(request.POST or None,instance=author)
    if request.method=="POST":
        if form.is_valid():
            author = form.save()
            # return redirect("detail-author", pk=author.id)
            return redirect("create-book",pk=author.id)
        context = {
            "form": form,
            "author": author,
            "books": books,
        }
    return render(request, 'partials/author_form.html', context)
