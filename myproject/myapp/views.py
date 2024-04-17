from django.shortcuts import render
from django.http import HttpResponse
from random import randint


def index(request):
    http_text = """
    <h1>Первый Django сайт</h1>
    <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
    Aenean commodo ligula eget dolor. Aenean massa. 
    Cum sociis natoque penatibus et magnis dis parturient montes, 
    nascetur ridiculus mus. Donec quam felis, ultricies nec, 
    pellentesque eu, pretium quis, sem. 
    Nulla consequat massa quis enim. 
    Donec pede justo, fringilla vel, aliquet nec, vulputate</p>
    """
    return HttpResponse(http_text)


def about(request):
    http_text = """
    <h1>О себе</h1>
    <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
    Aenean commodo ligula eget dolor. Aenean massa. 
    Cum sociis natoque penatibus et magnis dis parturient montes, 
    nascetur ridiculus mus. Donec quam felis, ultricies nec, 
    pellentesque eu, pretium quis, sem. 
    Nulla consequat massa quis enim. 
    Donec pede justo, fringilla vel, aliquet nec, vulputate</p>
    """
    return HttpResponse(http_text)


def heads_tails(request):
    numbers = randint(1, 2)
    if numbers == 1:
        return HttpResponse('heads')
    else:
        return HttpResponse('tails')


def cube(request):
    numbers = randint(1, 6)
    return HttpResponse(str(numbers))


def rnd(request):
    numbers = randint(1, 100)
    return HttpResponse(str(numbers))
