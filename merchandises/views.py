from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, get_object_or_404

from .forms import NewMerchandiseForm
from .models import Merchandise

# Create your views here.

def merch_detail(request, pk):
    merchandise = get_object_or_404(Merchandise, pk=pk)
    related_merchandises = Merchandise.objects.filter(category=merchandise.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'merchandise/merch_detail.html', {
        'merchandise': merchandise,
        'related_merchandises': related_merchandises
    })

@login_required 
def new_merch(request):
    form = NewMerchandiseForm

    return render(request, 'merchandise/form.html', {
        'form': form,
        'title': 'New Merchandise',

    })