from django.shortcuts import render
from .models import Equation

# Create your views here.
def index(request):
    equations = Equation.objects.all().order_by('-id')[:10]
    return render(request, 'calculator/index.html', {'equations': equations})