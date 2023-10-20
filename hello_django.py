from django.http import HttpResponse


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
