from django.shortcuts import render
from .models import Student
# Create your views here.
def home(request):
    return render(request, 'std/home.html', {})

def std_add(request):
    if request.method == 'POST':
        print('Added')
        std_roll = request.POST.get('roll')
        std_name = request.POST.get('name')
        std_email = request.POST.get('email')
        std_phone = request.POST.get('phone')
        std_address = request.POST.get('address')
    return render(request, 'std/std_add.html', {})