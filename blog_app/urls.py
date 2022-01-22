from django.urls import path
from .views import home_view, post_list, post_create, about_view, post_detail
from django.conf.urls.static import static
from django.conf import settings

app_name = "pages"

urlpatterns = [
    path('home/', home_view, name = 'home'),
    path('about/', about_view, name = 'about'),
    path('postlist/', post_list, name = 'list'),
    path('postcreate/', post_create, name = 'create'),
    path('postdetail/<slug:post_slug>', post_list, name = 'detail')

    # path('postlike/', like_post, name = 'like'),

]