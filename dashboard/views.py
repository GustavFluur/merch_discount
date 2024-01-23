from django.contrib.auth.decorators import login_required 
from django.shortcuts import render

from merchandises.models import Merchandise


@login_required 
def index(request):
    merchandises = Merchandise.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'merchandises': merchandises, 
    })

