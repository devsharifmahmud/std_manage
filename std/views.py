from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'std/home.html', {})

def std_add(request):
    if models.method == 'POST':

    return render(request, 'std/std_add.html', {})