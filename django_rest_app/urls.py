

from django.urls import path

from django_rest_app import views
urlpatterns = [
    path('api', views.snippet_list, name='snippet-list'),
    path('api/<int:pk>', views.snippet_details, name='snippet-detele'),


    path('api/decorate', views.snippet_list_decorate, name='snippet-list-decorate'),
    path('api/decorate/<int:pk>', views.snippet_details_decorate, name='snippet-list-decorate'),

]