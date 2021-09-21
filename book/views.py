from django import forms
from django.db import models
from django.shortcuts import redirect, render
from .models import Book
from author.models import Author
from authentication.models import CustomUser
from order.models import Order
from django.views.generic import View, UpdateView
from django.views.decorators.csrf import csrf_protect
from .forms import BooksForm
from django.http import HttpResponse
from django.db.models import Q


def book_by_id(request, book_id):
    book = Book.get_by_id(book_id)
    context = {
        'book': book
    }
    return render(request,'book/book_by_id.html',context)

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'GET':
        context = {
            'book': book,
            'title': 'dfds'
        }
        return render(request, 'book/delete_book.html', context)
    if request.method == 'POST':
        action = request.POST.get('button')
        
        if action == 'Delete_all':
            Book.delete_by_id(book_id)
            return redirect('book')

        if action == 'Delete_one':
            book.count -= 1
            book.update(count=book.count)
            return redirect('book')



    # if action == 'Delete_one':
    #     book = Book.get_by_id(book_id)
    #     if book.count > 1:
    #         book.count -= 1
    #         book.update(count=book.count)
    #     else:
    #         Book.delete_by_id(book_id)
        
    # elif action == 'Delete_all':
    #     Book.delete_by_id(book_id)


@csrf_protect
def get_all(request):
    if request.method == 'GET':
        return render(request, 'book/book.html', {'books': Book.get_all()})
    if request.method == 'POST':
        get_select_value = request.POST.get('opt')
        get_input_value = request.POST.get('title')
        if get_select_value == 'Show specific book (enter id)':
            return render(request, 'book/book.html', {'books': [Book.get_by_id(int(get_input_value))]})
        elif get_select_value == 'Show all books by name of author':
            return render(request, 'book/book.html', {'books': show_books_by_name_author(get_input_value)})
        elif get_select_value == 'Show all books sorted by name asc':
            return render(request, 'book/book.html', {'books': Book.objects.all().order_by('name')})
        elif get_select_value == 'Show all books sorted by name desc':
            return render(request, 'book/book.html', {'books': Book.objects.all().order_by('-name')})
        elif get_select_value == 'Show all books sorted by count':
            return render(request, 'book/book.html', {'books': Book.objects.all().order_by('count')})
        elif get_select_value == 'Show all unordered book':
            return render(request, 'book/book.html', {'books': get_unordered_books()})
        else:
            return render(request, 'book/book.html', {'books': Book.get_all()})


def show_books_by_name_author(get_input_value):
    res = []
    for elem in Book.get_all():
        for br in elem.authors.all():
            if br.name == get_input_value or br.surname == get_input_value or br.patronymic == get_input_value:
                res.append(elem)
    return res


def get_unordered_books():
    all_books = Book.get_all()
    all_orders = Order.get_all()
    get_all_ordered_books = []
    for book in all_books:
        for order in all_orders:
            if book.id == order.book.id:
                get_all_ordered_books.append(book)
    get_all_unordered_books = set(all_books) - set(get_all_ordered_books)
    return get_all_unordered_books

def add_book(request):
    
    if request.method == "POST":
        form = BooksForm(request.POST)
        if form.is_valid():
            if not check_book_in_library(form):
                form.save()
            return redirect('book')
    
    elif request.method == "GET":
        form = BooksForm()
        context = {
            'form': form
        }
        return render(request, 'book/add_book.html', context)


def check_book_in_library(form):
    '''THIS function checked if a book is in a library
    If true count of book increase by count witch user input in form'''
    try:
        book = Book.objects.get(name=form.cleaned_data['name'], authors=(form.cleaned_data['authors'][0]))
        book.count += form.cleaned_data['count']
        book.update(count=book.count)
        return True
    except (Book.DoesNotExist, Book.MultipleObjectsReturned):
        return False


class BookUpdateViews(UpdateView):
    model = Book
    template_name = 'book/add_book.html'
    fields = ['name', 'description', 'count', 'authors']
    success_url = '/book/'
    # form_class = BooksForm
# def update_book(request, book_id):
#     if request.method == "POST":
        
#     else:    
#         form = BooksForm()
#         book  = Book.get_by_id(book_id)
#         context = {
#          'form': form,
#          'book' : book
#         }
#         return render(request, 'book/update_book.html', context)