from typing import TYPE_CHECKING

from faker import Faker
from mixer.backend.django import mixer

if TYPE_CHECKING:
    from main.models import AudioContent, Page, PageBlock, TextContent, VideoContent


class Factory:
    faker = Faker()

    @classmethod
    def page(cls, **kwargs) -> "Page":
        return mixer.blend("main.Page", **kwargs)

    @classmethod
    def video_content(cls, **kwargs) -> "VideoContent":
        return mixer.blend("main.VideoContent", counter=0, **kwargs)

    @classmethod
    def audio_content(cls, **kwargs) -> "AudioContent":
        return mixer.blend("main.AudioContent", counter=0, **kwargs)

    @classmethod
    def text_content(cls, **kwargs) -> "TextContent":
        return mixer.blend("main.TextContent", counter=0, **kwargs)

    @classmethod
    def page_block(cls, page: "Page", **kwargs) -> "PageBlock":
        return mixer.blend("main.PageBlock", page=page, **kwargs)
