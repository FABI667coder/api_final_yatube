from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = routers.DefaultRouter()

router_v1.register(r'posts', PostViewSet, basename='post',)
router_v1.register(r'groups', GroupViewSet, basename='group',)
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment',
)
router_v1.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path(r'v1/api-token-auth/', views.obtain_auth_token),
    path(r'v1/', include(router_v1.urls)),
    path(r'v1/', include('djoser.urls.jwt')),
]
