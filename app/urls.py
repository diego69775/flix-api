from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('genero.urls')),
    path('api/v1/', include('ator.urls')),
    path('api/v1/', include('filme.urls')),
    path('api/v1/', include('reviews.urls')),
]
