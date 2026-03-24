from django.shortcuts import render
from .models import Student
# Create your views here.
def home(request):
    return render(request, 'std/home.html', {})

def std_add(request):
    if request.method == 'POST':
        print('Added')
        std_roll = request.POST.get('roll')
    return render(request, 'std/std_add.html', {})