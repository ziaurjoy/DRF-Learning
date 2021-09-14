
'''

from django.urls import path,include
from django.urls.resolvers import URLPattern
from class_based_view import views

from class_based_view.serializer import UserSerializer
from django.contrib.auth.models import User

urlpatterns = [
    path('list', views.SnippetList.as_view(), name='snippet-list'),
    path('details/<int:pk>', views.SnippetDetail.as_view(), name='snippet-details'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/list/', views.ListUsers.as_view()),
    # path('users/list/generic', views.UserList_Generic.as_view()),

    path('users/list/generic', views.UserList_Generic.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name='user-list'),

    path('users/hello/', views.hello_world, name='hello'),

    
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]


'''


from class_based_view.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users/list', UserViewSet, basename='user')
urlpatterns = router.urls