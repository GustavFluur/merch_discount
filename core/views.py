from django.shortcuts import render

from merchandises.models import Category, Merchandise

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