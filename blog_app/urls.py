from django.urls import path
from .views import home_view, post_list, post_create, like_post
from django.conf.urls.static import static
from django.conf import settings

app_name = "pages"

urlpatterns = [
    path('home/', home_view),
    path('postlist/', post_list, name = 'list'),
    path('postcreate/', post_create, name = 'create'),
    path('postlike/', like_post, name = 'like'),

]