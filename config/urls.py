from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from blog.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("maqola/", include("blog.urls")),

] + static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)

