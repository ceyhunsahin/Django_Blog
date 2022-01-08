from django.shortcuts import render, redirect
from .models import Post, Like
from .forms import PostForm


def home_view(request):
    return render(request, 'pages/home_page.html',{'nbar': 'home', 'username': request.user})

def post_list(request) :
    qs = Post.objects.all()
    user = request.user
    context = {
        'object_list' : qs,
        'user' : user
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
            print(request.user.username)
            post.save()
            return redirect('pages:list')
    context = {
        'form': form
    }
    return render(request, 'pages/post_create.html', context)

def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        print(post_id)
        post_obj = Post.objects.get(id = post_id)
        print(post_obj)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else : post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user = user, post_id=post_id)
        if not created:
            if like.value == 'Like' :
                like.value = 'Unlike'

            like.save()

        return redirect('pages:list')
# Create your views here.
