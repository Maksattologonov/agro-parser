from django.db import models


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    image_id = models.URLField(verbose_name='Изображение', unique=True)
    text = models.TextField(verbose_name='Текст')
    author = models.CharField(max_length=255, verbose_name='Автор')
    last_updated = models.DateField(verbose_name='Последнее обновление')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        db_table = 'news'


class Images(models.Model):
    image = models.ImageField(upload_to='Media/%yyear/%mmonth/%dday')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = "Изображении"
        db_table = 'images'


class Links(models.Model):
    link = models.TextField(verbose_name="Ссылки")

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
        db_table = 'links'
