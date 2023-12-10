from django.shortcuts import render, get_object_or_404
from .models import Merchandise

# Create your views here.

def merch_detail(request, pk):
    merchandise = get_object_or_404(Merchandise, pk=pk)

    return render(request, 'merchandise/merch_detail.html', {
        'merchandise': merchandise
    })
