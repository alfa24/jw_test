from django.db import models
from model_utils.models import TimeStampedModel


class BaseContent(TimeStampedModel):
    title = models.CharField('Заголовок', max_length=200)
    counter = models.PositiveIntegerField('Счетчик', default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        abstract = True


class VideoContent(BaseContent):
    video = models.FileField('Видеофайл', upload_to='video')
    subtitle = models.FileField('Субтитры', upload_to='subtitle')

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class AudioContent(BaseContent):
    audio = models.FileField('Аудиофайл', upload_to='audio')
    bitrate = models.IntegerField('Битрейт', default=0)

    class Meta:
        verbose_name = 'Аудио'
        verbose_name_plural = 'Аудио'


class TextContent(BaseContent):
    text = models.TextField('Текст')

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Текст'
