from django.shortcuts import redirect, render

# Create your views here.


from class_based_view.models import Snippet


from class_based_view.models import Snippet
from class_based_view.serializer import SnippetSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from rest_framework.renderers import TemplateHTMLRenderer



"""
class SnippetList(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializers = SnippetSerializer(snippets, many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = SnippetSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_401_UNAUTHORIZED)


class SnippetDetail(APIView):
    def get_objects(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        snippet = self.get_objects(pk)
        serializers = SnippetSerializer(snippet)
        return Response(serializers.data, status=status.HTTP_201_CREATED)

    def put(self,request, pk, format = None):
        snippet = self.get_objects(pk)
        serializers = SnippetSerializer(snippet, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self,request, pk, format = None):
        snippet = self.get_objects(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
"""



# Templates Data Sending

class SnippetList(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'snippet_list.html'

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        context = {
            'snippets': snippets
        }
        return Response(context)
    
    def post(self, request, format=None):
        serializers = SnippetSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_401_UNAUTHORIZED)


class SnippetDetail(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'snippet_detail.html'

    def get_objects(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        snippet = self.get_objects(pk)
        serializers = SnippetSerializer(snippet)
        context = {
            'serializer': serializers, 
            'snippet': snippet
            }
        return Response(context)

    def put(self,request, pk, format = None):
        snippet = self.get_objects(pk)
        serializers = SnippetSerializer(snippet, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return redirect('snippet-list')

        context = {
            'serializer': serializers, 
            'snippet': snippet
            }
        return Response(context)

    def delete(self,request, pk, format = None):
        snippet = self.get_objects(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)