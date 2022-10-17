from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

# Create your views here.

def home(request):
    post = Post.objects.all()
    context = {'posts':post}
    return render(request, "blog/tech-index.html", context)

def createpost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post added successfully')
            return redirect('home')
    context = {'form':form}
    return render(request, 'blog/createpost.html', context)

def updatepost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
                form.save()
                messages.success(request, 'Post updated successfully')
                return redirect('home')
    context = {'form':form}
    return render(request, 'blog/updatepost.html', context)
  
def deletepost(request, pk):
    post = Post.objects.filter(id=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post removed successfully')
        return redirect('home')
    return render(request, 'blog/deletepost.html')

def gadgets(request):
    return render(request, 'blog/tech-category-01.html')

def contact(request):
    return render(request, 'blog/tech-contact.html')
 