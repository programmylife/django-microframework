from django.http import HttpResponse

from blog.models import Post


def hello_world(request):
    return HttpResponse(Post.objects.all().get(id=1).body)


def second_post(request):
    return HttpResponse(Post.objects.all().get(id=2).body)


def third_post(request):
    return HttpResponse(Post.objects.all().get(id=3).body)


def fourth_post(request):
    return HttpResponse(Post.objects.all().get(id=4).body)
