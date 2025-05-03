from django.urls import path
from django.urls import include, path

from polls import admin

from . import views

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]