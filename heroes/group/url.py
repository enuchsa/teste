from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from heroes.group.views import GropuList, GroupDetails

url_groups = [
    path('grupos/', GropuList.as_view()),
    path('grupos/<int:pk>/', GroupDetails.as_view()),
]

url_groups = format_suffix_patterns(url_groups)
