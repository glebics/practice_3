from django.urls import path
from .views import DogList, DogDetail, BreedList, BreedDetail
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# Настройка для генерации схемы и документации
schema_view = get_schema_view(
    openapi.Info(
        title="Dog API",
        default_version='v1',
        description="API для управления собаками и породами",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('api/dogs/', DogList.as_view(), name='dog-list'),
    path('api/dogs/<int:id>/', DogDetail.as_view(), name='dog-detail'),
    path('api/breeds/', BreedList.as_view(), name='breed-list'),
    path('api/breeds/<int:id>/', BreedDetail.as_view(), name='breed-detail'),


    # URL для Swagger и ReDoc
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
