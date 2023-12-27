from django.contrib import admin
from django.urls import path, include
from heroes import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.HeroViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
