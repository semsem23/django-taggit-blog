from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from taggit.models import Tag
from .forms import PostForm
from django.template.defaultfilters import slugify

def post_list(request):
    posts = Post.objects.all()
    
    context = {'posts': posts}
    return render(request, 'post_list.html', context)
 
def post_detail(request, slug):
    posts = get_object_or_404(Post, slug=slug)
    
    context = {'posts': posts}
    return render(request, 'post_detail.html', context)

def tagged(request, slug):
     tag = get_object_or_404(Tag, slug=slug)
     posts = Post.objects.filter(tags=tag)
     
     context = {'posts': posts, 'tag':tag}
     return render(request, 'tags.html', context)

def create_tags(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.slug = slugify(newpost.title)
            newpost.save()
            
            form.save_m2m()
        return redirect('post_list')
    else:
        form = PostForm()
        context = {'form': form}
    return render(request, 'create_tags.html', context)