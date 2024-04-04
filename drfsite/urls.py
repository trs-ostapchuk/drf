from django.contrib import admin
from django.urls import path

from someapp.views import WomenAPIView, WomenAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/womenlist/', WomenAPIView.as_view()),
    path('api/v1/womenl/', WomenAPI.as_view()),
]
