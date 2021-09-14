from django.core.exceptions import ValidationError
from django.db import models
from model_utils.models import TimeStampedModel

from main.models import VideoContent, AudioContent, TextContent


class Page(TimeStampedModel):
    title = models.CharField('Заголовок', max_length=200)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class PageBlock(TimeStampedModel):
    custom_order = models.PositiveIntegerField(default=0, blank=False, null=False)
    page = models.ForeignKey(Page, related_name='blocks', verbose_name='Страница', on_delete=models.CASCADE)

    content_video = models.ForeignKey(
        VideoContent,
        verbose_name='Видео',
        related_name='blocks',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    content_audio = models.ForeignKey(
        AudioContent,
        verbose_name='Аудио',
        related_name='blocks',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    content_text = models.ForeignKey(
        TextContent,
        verbose_name='Текст',
        related_name='blocks',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    def clean_content(self):
        content_fields = [x.name for x in self._meta.fields if x.name.startswith('content_')]
        content_type = None
        errors = {}
        for field in content_fields:
            value = getattr(self, field)
            if not value:
                continue

            if content_type:
                errors[field] = ValidationError('Должен быть выбран только один вид контента.')
            else:
                content_type = field

        if not content_type:
            errors = {
                x: ValidationError('Должен быть выбран хотя бы один вид контента.')
                for x in content_fields
            }

        if errors:
            raise ValidationError(errors)

    def full_clean(self, exclude=None, validate_unique=True):
        self.clean_content()
        return super().full_clean(exclude, validate_unique)

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'
        ordering = ['custom_order']
