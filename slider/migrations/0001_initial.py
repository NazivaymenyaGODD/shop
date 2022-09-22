# Generated by Django 4.1 on 2022-09-22 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_image', models.ImageField(blank=True, upload_to='sliderimg', verbose_name='Фото слайдера')),
                ('slider_title', models.CharField(blank=True, max_length=100, verbose_name='Заголовок')),
                ('slider_text', models.CharField(blank=True, max_length=200, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
    ]