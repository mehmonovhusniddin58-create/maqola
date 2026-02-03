
from django.urls import path
from blog.views import detail

urlpatterns = [
    path("detail/<int:id>", detail, name="detail")
]
