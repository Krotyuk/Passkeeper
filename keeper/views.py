from django.shortcuts import render
from .models import accessPost
from django.shortcuts import render, get_object_or_404
from .forms import accessForm
from django.shortcuts import redirect


# Create your views here.
def access_list(request):
    listOfAccess = list(accessPost.objects.all())

    return render(request, 'keeper/access_list.html', {'listOfAccess': listOfAccess})

def access_detail(request, pk):
    access_detail = get_object_or_404(accessPost, pk=pk)
    return render(request, 'keeper/access_detail.html', {'access_detail': access_detail})

def access_new(request):
    if request.method == "POST":
        form = accessForm(request.POST)
        if form.is_valid():
            accessPost = form.save(commit=False)
            accessPost.author = request.user
            accessPost.save()
            return redirect('access_detail', pk=accessPost.pk)
    else:
        form = accessForm()
    return render(request, 'keeper/access_edit.html', {'form': form})

def access_edit(request, pk):
    post = get_object_or_404(accessPost, pk=pk)
    if request.method == "POST":
        form = accessForm(request.POST, instance=post)
        if form.is_valid():
            accessPost = form.save(commit=False)
            accessPost.author = request.user

            accessPost.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = accessForm(instance=post)
    return render(request, 'blog/access_edit.html', {'form': form})

def access_delete(request, pk):
    listOfAccess = accessPost.objects.filter(pk=pk).delete()
    return render(request, 'keeper/access_list.html', {'listOfAccess': listOfAccess})