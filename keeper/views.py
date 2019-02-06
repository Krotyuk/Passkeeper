from django.shortcuts import render
from .models import accessPost
from django.shortcuts import render, get_object_or_404



# Create your views here.
def access_list(request):
    listOfAccess = list(accessPost.objects.all())


    return render(request, 'keeper/access_list.html', {'listOfAccess': listOfAccess})

def access_detail(request, pk):
    access_detail = get_object_or_404(accessPost, pk=pk)
    return render(request, 'keeper/access_detail.html', {'access_detail': access_detail})