from django.shortcuts import render, redirect
from order.models import Order
from .models import Author
from authentication.models import CustomUser
from book.models import Book
from django.views.generic import View, DetailView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_protect
from .forms import *


@csrf_protect
def get_all(request):
    get_all_books = Book.get_all()
    get_all_authors = Author.get_all()
    if request.method == 'GET':
        return render(request, 'author/author.html', {'books': get_all_books, 'authors': get_all_authors})
    if request.method == 'POST':
        get_select_value = request.POST.get('opt')
        get_input_value = request.POST.get('title')
        if get_select_value == 'Show specific author with his books (enter id)':
            return render(request, 'author/author.html', {'books': get_all_books, 'authors': [Author.get_by_id(int(get_input_value))]})
        else:
            return render(request, 'author/author.html', {'books': get_all_books, 'authors': get_all_authors})


def add_author(request):
    error = ''
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author')
        else:
            error = 'Wrong form'

    form = AuthorForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'author/add_author.html', data)


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author/author_details.html'
    context_object_name = 'author_details'
    extra_context = {'auth_books': Book.get_all()}


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'author/update_author.html'
    form_class = AuthorForm
    context_object_name = 'author_update'


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'author/delete_author.html'
    success_url = '/author/'
    context_object_name = 'author_delete'


