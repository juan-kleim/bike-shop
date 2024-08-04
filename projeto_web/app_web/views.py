from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def home(request):
    return render(request, 'users/home.html')

def users(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = UserForm()

    form.fields['Texto'].widget.attrs.update({
        'class': 'form-control custom-textbox',
        'placeholder': 'Texto aqui'
    })

    context = {
        'form': form,
        'users': User.objects.all()
    }

    return render(request, 'users/users.html', context)


