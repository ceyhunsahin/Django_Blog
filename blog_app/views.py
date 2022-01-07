from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def home_view(request):
    return render(request, 'pages/home_page.html')

def post_list(request) :
    qs = Post.objects.all()
    print(qs)
    context = {
        'object_list' : qs
    }
    return render(request, 'pages/post_list.html', context)

def post_create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
    # form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect('pages:list')
    context = {
        'form': form
    }
    return render(request, 'pages/post_create.html', context)


# Create your views here.
