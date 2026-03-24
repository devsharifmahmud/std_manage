from django.shortcuts import render,redirect
from .models import Student
# Create your views here.
def home(request):
    std = Student.objects.all()
    return render(request, 'std/home.html', {'std':std})

def std_add(request):
    if request.method == 'POST':
        print('Added')
        #retreive the user inputs
        std_roll = request.POST.get('roll')
        std_name = request.POST.get('name')
        std_email = request.POST.get('email')
        std_phone = request.POST.get('phone')
        std_address = request.POST.get('address')

        #create an objects for models
        s = Student()
        s.roll = std_roll
        s.name = std_name
        s.email = std_email
        s.phone = std_phone
        s.address = std_address
        s.save()
        return redirect('/std/home')

    return render(request, 'std/std_add.html', {})