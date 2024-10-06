from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name=u'Название')
    text = models.TextField(verbose_name=u'Текст')
    published_at = models.DateTimeField(verbose_name=u'Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name=u'Изображение',)
    tags = models.ManyToManyField('Tag', related_name='articles', 
                                    verbose_name=u'Разделы', through='Scope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):

    name = models.CharField(max_length=50, verbose_name=u'Название')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name

class Scope(models.Model):

    article = models.ForeignKey(Article, on_delete=models.CASCADE, 
                                verbose_name=u'Название статьи', related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, 
                            verbose_name=u'Название раздела', related_name='scopes')
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        verbose_name = 'Тематики статьи'
        verbose_name_plural = 'Тематики статей'


