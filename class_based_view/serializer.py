
from class_based_view.models import Snippet
from rest_framework import serializers

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = '__all__'
    
