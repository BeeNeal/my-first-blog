from django.shortcuts import render, get_object_or_404, redirect
# The dot before models means current directory or current application. Both 
# views.py and models.py are in the same directory. This means we can use . and 
# the name of the file (without .py). Then we import the name of the model.
from .models import Post
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    # good practice to design a nice "page not found" error page
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # not commiting until we add the author, usually will not use commit.false
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})