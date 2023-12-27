from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from heroes.hero.url import url_heroes
from heroes.group.url import url_groups
from heroes.auth.url import url_auth


router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token, name='auth')
]

urlpatterns += [
    *router.urls,
    *url_heroes,
    *url_groups,
    *url_auth
]
