from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Hello World from Django!")
