from django.shortcuts import render
from .models import Data
from django.db.models import Q
# Create your views here.
def index(request):
    if 'q' in request.GET:
        q=request.GET['q']
        # data=Data.objects.filter(last_name__icontains=q)
        multiple_q=Q(Q(firse_name__icontains=q)| Q(last_name__icontains=q))
        data=Data.objects.filter(multiple_q)

    else:
        data=Data.objects.all()

    
   
    content={
        'data':data
    }
    return render(request,'dashboared/index.html',content)