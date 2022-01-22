from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import Post, Like, Category, Comment, PostView
from .forms import PostForm
from django.contrib.auth.models import User
from django.urls import reverse


def home_view(request):
    return render(request, 'pages/home_page.html',{'nbar': 'home', 'username': request.user})

def post_list(request) :
    qs = Post.objects.all()
    xx = User.objects.all ()
    print('xxxxxx',xx)
    user = request.user
    context = {
        'object_list' : qs,
        'user' : user
    }
    # post1 = User.objects.all()
    # print('post1', post1)
    # post2 = Like.objects.filter(post__title='ceyhun')
    # print ('post2', post2)
    # post3 = Like.objects.filter(user__username='john')
    # print ('post3', post3)
    # blogs = PostView.objects.filter(user__id = '1')
    # print('blog', blogs)
    # post4 = Post.objects.filter(category__name__icontains = 'django' )
    # print("post4", post4)
    if qs_slug != None:
        category_page = get_object_or_404(Category, slug = category_slug)
        courses = Course.objects.filter(available=True, category= category_page)
    if request.method == 'POST':
        post_id = request.POST.get ('post_id')
        print (post_id)
        post_obj = Post.objects.get (id=post_id)
        print (post_obj)

        if user in post_obj.liked.all ():
            post_obj.liked.remove (user)
        else:
            post_obj.liked.add (user)

        like, created= Like.objects.get_or_create (user=user, post_id=post_id)
        print(Like.objects.get_or_create (user=user, post_id=post_id))
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else :
                like.value = 'Like'
            like.save ()
            # return redirect ('pages:list')

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
    return redirect('pages:list')
def about_view(request) :
    return render(request, 'pages/about.html')

def post_detail(request):
    return render(request, 'pages/post_list.html')
# def like_post(request):
#     user = request.user
#     if request.method == 'POST':
#         post_id = request.POST.get('post_id')
#         print(post_id)
#         post_obj = Post.objects.get(id = post_id)
#         print(post_obj)
#
#         if user in post_obj.liked.all():
#             post_obj.liked.remove(user)
#         else : post_obj.liked.add(user)
#
#         like, created = Like.objects.get_or_create(user = user, post_id=post_id)
#         if not created:
#             if like.value == 'Like' :
#                 like.value = 'Unlike'
#
#             like.save()
#
#         return redirect('pages:list')
# Create your views here.
def like_post(request):
    pass


