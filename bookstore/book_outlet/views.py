from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.
from django.db.models import Avg
from .models import Book


def index(req):

    books = Book.objects.all()
    num_books = books.count()
    avg_rating = books.aaggregate(Avg("rating"))

    return render(req, 'book_outlet/index.html', {
        "books": books,
        "total_number_of_books": num_books,
        "average": avg_rating
    })


def book_details(req, slug):

    # try:
    #     book = Book.objects.get(id=id)
    # except:
    #     raise Http404()

    book = get_object_or_404(Book, slug=slug)
    return render(req, "book_outlet/book_details.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })
