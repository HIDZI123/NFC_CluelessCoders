from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request,"main/index.html",
    {
        "parts":Part.objects.all(),
    })

def disease_search(request):
    if request.method == 'POST':
        searched=request.POST['searched']   

    else:
        searched=''
        
    diseases = Disease.objects.filter(name__contains=searched)

    return render(request, 'main/disease_search.html', 
        {'searched':searched,
        'diseases': diseases})


def disease(request,disease_id):
    disease=Disease.objects.get(id=disease_id)
    part=disease.part.all()


    return render(request,"main/disease.html",
    {"disease":disease,"parts":part})


def bodypart(request,part_id):
    part=Part.objects.get(id=part_id)
    disease=part.disease.all()

    return render(request,"main/bodyparts.html",
    {"parts":part,"diseases":disease,})