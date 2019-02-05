from django.shortcuts import render

# Create your views here.
def access_list(request):
    return render(request, 'keeper/access_list.html', {})