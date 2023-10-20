from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path

settings.configure(
    ROOT_URLCONF=__name__,
    DEBUG=True,
)


def hello_world(request):
    return HttpResponse("Hello, Django!")


def second_post(request):
    return HttpResponse("This is my second blog post. I'm still figuring this whole thing out.")


def third_post(request):
    return HttpResponse(
        "This is my third blog post. I'm feeling more comfortable with this whole thing, and I'm going to try to write a bit more. "
    )


def fourth_post(request):
    return HttpResponse(
        "Hot dogs are not a sandwich. In this blog post I will first define the meaning of sandwich, then I will ???? which will conclusively prove that hot dogs are indeed not sandwiches."
    )


urlpatterns = [
    path("hello-world", hello_world),
    path("second-post", second_post),
    path("third-post", third_post),
    path("fourth-post", fourth_post),
]

application = WSGIHandler()

if __name__ == "__main__":
    execute_from_command_line()
