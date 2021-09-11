

from django.urls import path

from django_rest_app.views import snippet_details, snippet_list
urlpatterns = [
    path('api', snippet_list, name='snippet-list'),
    path('api/<int:pk>', snippet_details, name='snippet-detele'),
]