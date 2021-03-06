from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet


router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register('posts/(?P<post_id>\\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls)),
]


# urlpatterns += [
#     path('api-token-auth/', views.obtain_auth_token),
#     # Djoser создаст набор необходимых эндпоинтов
#     # Базовые для управления пользователями в Django:
#     path('auth/', include('djoser.urls')),
#     # JWT-эндпоинты, для управления JWT-токенами
#     path('auth/', include('djoser.urls.jwt')),
#     # Все зарегистрированные в router пути доступны в router.urls
#     path('posts/<int:pk>/comments', CommentViewSet),
#     path('', include(router.urls)),
