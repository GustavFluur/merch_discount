from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewMerchandiseForm, EditMerchandiseForm
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
    if request.method == 'POST':
        form = NewMerchandiseForm(request.POST, request.FILES)

        if form.is_valid():
            merchandise = form.save(commit=False) #for creating a new product without saving into DB
            merchandise.created_by = request.user
            merchandise.save()

            return redirect('merchandise:detail', pk=merchandise.id)
    else:        
        form = NewMerchandiseForm()

    return render(request, 'merchandise/form.html', {
        'form': form,
        'title': 'New Merchandise',

    })


@login_required 
def edit_merch(request, pk):
    merchandise = get_object_or_404(Merchandise, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        form = EditMerchandiseForm(request.POST, request.FILES, instance=merchandise)

        if form.is_valid():
            form.save()

            return redirect('merchandise:detail', pk=merchandise.id)
    else:        
        form = EditMerchandiseForm(instance=merchandise)

    return render(request, 'merchandise/form.html', {
        'form': form,
        'title': 'Edit Merchandise',

    })


@login_required
def delete_merch(request, pk):
    merchandise = get_object_or_404(Merchandise, pk=pk, created_by=request.user)
    merchandise.delete()

    return redirect('dashboard:index')