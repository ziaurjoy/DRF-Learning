
from django.contrib.auth.models import User

from class_based_view.models import Snippet
from rest_framework import serializers

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
   # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username')
    
