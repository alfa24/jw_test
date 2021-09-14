from rest_framework import viewsets

from api.v1.serializers import PageSerializer
from main.models import Page


class PageViewsSet(viewsets.ReadOnlyModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
