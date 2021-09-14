from rest_framework import viewsets

from api.v1.serializers import PageSerializer
from main.models import Page
from main.tasks import inc_counter_by_page_task


class PageViewsSet(viewsets.ReadOnlyModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        inc_counter_by_page_task.delay(instance.id)
        return super().retrieve(request, *args, **kwargs)
