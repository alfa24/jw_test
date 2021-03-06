from django.urls import include, path
from rest_framework import routers

from api.v1 import views

app_name = "api"
router = routers.DefaultRouter()
router.register("pages", views.PageViewsSet, basename="pages")

urlpatterns = [
    path("", include(router.urls)),
]
