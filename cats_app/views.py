from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from cats_app.models import Cats


def ping(request):
    return HttpResponse('Cats Service. Version 0.3\n')


def cats(request):
    query = Cats.objects.values('name', 'color', 'tail_length', 'whiskers_length')
    print(query)
    # query = query.filter(name='Tihon')
    # data = serializers.serialize('json', query, fields=('name', 'color', 'tail_length', 'whiskers_length'))
    # data = serializers.serialize('json', query, fields=('name', 'color', 'tail_length', 'whiskers_length'))
    data = list(query)
    print(data)
    return JsonResponse(data, safe=False)


def cat(request):
    return HttpResponse('Cat\n')


