

from django.urls import path
from django.urls.resolvers import URLPattern
from class_based_view import views
urlpatterns = [
    path('list', views.SnippetList.as_view(), name='snippet-list'),
    path('details/<int:pk>', views.SnippetDetail.as_view(), name='snippet-details'),
]