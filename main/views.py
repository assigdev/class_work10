from django.shortcuts import render
from .forms import TestForm
from .models import Test


def home(request):
    is_valid = False
    form = TestForm(initial={'name': 'Ваше имя'})
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            age = form.cleaned_data.get('age')
            birth = form.cleaned_data.get('birth')
            Test.objects.create(name=name, age=age, birth=birth)
            is_valid = True
    return render(request, 'home.html', {'form': form, 'is_valid': is_valid})


# def home(request):
#     if request.method == 'POST':
#         form = TestForm(request.POST)
#         if form.is_valid():
#             return render(request, 'home.html', {'is_valid': True})
#         else:
#             return render(request, 'home.html', {'form': form})
#     return render(request, 'home.html', {'form': TestForm()})
