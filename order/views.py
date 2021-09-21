from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm
from django import forms
from author.models import Author
from authentication.models import CustomUser
from book.models import Book
from django.views.generic import View, DetailView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_protect
import datetime

def get_all(request):
    get_all_orders = Order.get_all()
    if request.method == 'GET':
        return render(request, 'order/order.html', {'orders': get_all_orders})
    elif request.method == 'POST':
        get_select_value = request.POST.get('opt')
        get_input_value = request.POST.get('title')
        if get_select_value == 'Show all users who does not hand over books on time':
            return render(request, 'order/order.html', {'orders': unpunctual_users()})
        elif get_select_value == 'Show all books ordered by specific user (enter user id)':
            return render(request, 'order/order.html', {'orders': show_orders_of_specific_user(int(get_input_value))})
        elif get_select_value == 'Show all orders sorted by created date':
            return render(request, 'order/order.html', {'orders': Order.objects.all().order_by('created_at')})
        elif get_select_value == 'Show all orders sorted by planed date':
            return render(request, 'order/order.html', {'orders': Order.objects.all().order_by('plated_end_at')})
        else:
            return render(request, 'order/order.html', {'orders': get_all_orders})


def show_orders_of_specific_user(get_input_value):
    result = []
    for elem in Order.get_all():
        if elem.user.id == get_input_value:
            result.append(elem)
    return result


def unpunctual_users():
    now = datetime.datetime.now().timestamp()
    result = []
    for elem in Order.get_all():
        if elem.end_at:
            if elem.end_date.timestamp() > elem.plated_end_at.timestamp():
                result.append(elem)
        else:
            if elem.plated_end_at.timestamp() < now:
                result.append(elem)
    return result

# ORDERS
#         <option>Show all books of specific user (enter user id)</option>
#         <option>Show all orders sorted by created date</option>
#         <option>Show all orders sorted by planed date</option>
#         <option>Show all users who does not hand over books on time</option>

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            Order.objects.create(**form.cleaned_data)
            return redirect('order')
    else:
        pass

    form = OrderForm()
    return render(request, 'order/add_order.html', {'form': form})


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order/delete_order.html'
    success_url = '/order/'
    context_object_name = 'order_delete'


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order/update_order.html'
    fields = ['plated_end_at', 'end_at']
    context_object_name = 'order_update'

