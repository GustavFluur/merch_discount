from django.shortcuts import render, redirect

from merchandises.models import Category, Merchandise
from .forms import RegisterForm

# Create your views here.
def index(request):
    merchandises = Merchandise.objects.filter(is_sold=False)
    # for another page, all products needs to be shown
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'merchandises': merchandises, 

    })

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def register(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:        
        form = RegisterForm()
    


    return render(request, 'core/register.html', {
        'form': form
    })