from django.urls import reverse
from rest_framework import serializers

from main.models import AudioContent, Page, PageBlock, TextContent, VideoContent


class ContentVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoContent
        fields = ["id", "title", "counter", "video", "subtitle"]


class ContentAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioContent
        fields = ["id", "title", "counter", "audio", "bitrate"]


class ContentTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextContent
        fields = ["id", "title", "counter", "text"]


class PageBlockSerializer(serializers.ModelSerializer):
    content_video = ContentVideoSerializer()
    content_audio = ContentAudioSerializer()
    content_text = ContentTextSerializer()

    class Meta:
        model = PageBlock
        fields = ["id", "content_video", "content_audio", "content_text"]


class PageListSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    def get_absolute_url(self, obj):
        url = reverse("api:pages-detail", args=(obj.id,))
        request = self.context.get("request")
        absolute_url = request.build_absolute_uri(url) if request else url
        return absolute_url

    class Meta:
        model = Page
        fields = ["id", "title", "absolute_url"]


class PageSerializer(serializers.ModelSerializer):
    blocks = PageBlockSerializer(many=True)

    @classmethod
    def many_init(cls, *args, **kwargs):
        return PageListSerializer(*args, **kwargs, many=True)

    class Meta:
        model = Page
        fields = ["id", "title", "blocks"]
