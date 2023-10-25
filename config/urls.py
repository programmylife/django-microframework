from django.contrib import admin
from django.urls import path

from blog.views import hello_world, second_post, third_post, fourth_post

urlpatterns = [
    path("hello-world", hello_world),
    path("second-post", second_post),
    path("third-post", third_post),
    path("fourth-post", fourth_post),
    path("admin/", admin.site.urls),
]
