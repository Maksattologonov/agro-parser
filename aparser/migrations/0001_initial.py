# Generated by Django 3.2.5 on 2021-07-16 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Media/%yyear/%mmonth/%dday')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображении',
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(verbose_name='Ссылки')),
            ],
            options={
                'verbose_name': 'Ссылка',
                'verbose_name_plural': 'Ссылки',
                'db_table': 'links',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('image_id', models.URLField(verbose_name='Изображение')),
                ('text', models.TextField(verbose_name='Текст')),
                ('author', models.CharField(max_length=255, verbose_name='Автор')),
                ('last_updated', models.DateField(verbose_name='Последнее обновление')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'db_table': 'news',
            },
        ),
    ]