from django.shortcuts import render
from django.http import HttpResponse


def ping(request):
    return HttpResponse('Cats Service. Version 0.3\n')


def cat(request):
    pass


def cats(request):
    pass
