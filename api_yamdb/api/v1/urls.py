from django.urls import include, path
from rest_framework import routers

from .views import (CategoryViewSet,
                    CommentViewSet,
                    CreateUserView,
                    GenreViewSet,
                    ReviewViewSet,
                    TitleViewSet,
                    TokenObtainView,
                    UsersViewSet)

v1_router = routers.DefaultRouter()

v1_router.register('users', UsersViewSet)
v1_router.register('categories', CategoryViewSet)
v1_router.register('genres', GenreViewSet)
v1_router.register('titles', TitleViewSet)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='review'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comment'
)

auth_urls = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('token/', TokenObtainView.as_view(), name='token'),
]

urlpatterns = [
    path('', include(v1_router.urls)),
    path('auth/', include(auth_urls)),
]
