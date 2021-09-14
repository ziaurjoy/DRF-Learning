from django.shortcuts import render
from class_based_view import serializer

# Create your views here.


from class_based_view.models import Snippet


from class_based_view.models import Snippet
from class_based_view.serializer import SnippetSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import serializers, status

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






from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer







# Class-based Views

from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response

from django.contrib.auth.models import User

class ListUsers(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        usernames = [user.name for user in User.objects.all()]
        return Response(usernames)





# Function-based Views
from rest_framework.decorators import api_view,throttle_classes




# @api_view()
# def hello_world(request):
#     return Response({"Message": 'Hello, world'})


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"Message": 'Got some data','data': request.data})
    return Response({"Message": 'Hello, world'})





# from rest_framework.throttling import UserRateThrottle

# class OncePerDayUserThrottle(UserRateThrottle):
#     rate = '1/day'

# @api_view(['GET'])
# @throttle_classes([OncePerDayUserThrottle])
# def view(request):
#     return Response({"message": "Hello for today! See you tomorrow!"})











# Generic views

from class_based_view.serializer import UserSerializer
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


# class UserList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminUser]

class UserList_Generic(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)





# ViewSets




from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from class_based_view.serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

user_list = UserViewSet.as_view({'get': 'list'})
user_detail = UserViewSet.as_view({'get': 'retrieve'})







