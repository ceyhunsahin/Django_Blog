from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    return 'blog/{0}/{1}'.format(instance.author.id, filename)

class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta :
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name
# Create your models here.
class Post(models.Model):
    OPTIONS = (
        ('drft', 'Draft'),
        ('pblshd', 'published')
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, default='django_1.jpeg')
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')
    category = models.ForeignKey(Category, on_delete = models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS,default='drft')
    slug = models.SlugField(blank= True, unique=True)
    def __str__(self):
        return self.title

    @property
    def num_like(self):
        return str (self.like.all ().count ())

class Comment(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username
LIKE_CHOICES = (
    ('like' , 'Like'),
    ('unlike', 'Unlike')
)
class Like(models.Model) :
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length= 10)

    def __str__(self):
        return self.user.username



class PostView(models.Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE)
    post = models.ForeignKey (Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField (auto_now_add=True)

    def __str__(self):
        return self.user.username