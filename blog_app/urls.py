from django.urls import path
from .views import home_view, post_list,post_create
from django.conf.urls.static import static
from django.conf import settings

app_name = "pages"

urlpatterns = [
    path('', home_view),
    path('postlist/', post_list, name = 'list'),
    path('postcreate/', post_create, name = 'create')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)