from django.shortcuts import render
from rest_framework import serializers
from django_rest_app.models import Snippet
from django_rest_app.serializers import SnippetSerializer

from django.http import JsonResponse, HttpResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serialiser = SnippetSerializer(snippets, many=True)
        return JsonResponse(serialiser.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serialiser = SnippetSerializer(data=data)
        if serialiser.is_valid():
            serialiser.save()
            return JsonResponse(serialiser.data, status = 201)
        return JsonResponse(serialiser.errors, status = 401)





@csrf_exempt
def snippet_details(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data, status = 201)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status = 401)
    
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)



