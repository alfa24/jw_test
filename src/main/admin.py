from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin

from main.models import VideoContent, AudioContent, TextContent, Page, PageBlock

admin.site.register(VideoContent)
admin.site.register(AudioContent)
admin.site.register(TextContent)


class PageBlockInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PageBlock
    extra = 0


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    exclude = []
    inlines = [PageBlockInline]
    search_fields = [
        'title__istartswith',
        *[f'blocks__{x.name}__title__istartswith' for x in PageBlock.get_content_fields()]
    ]
