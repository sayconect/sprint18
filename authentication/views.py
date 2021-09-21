
from django.shortcuts import redirect, render
from .forms import UsersFrom
# Create your views here.

def creat_user(request):
    if request.method == 'POST':
        form = UsersFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = UsersFrom()
    context = {
        'form': form
    }
    return render(request, 'authentication/create_user.html', context)