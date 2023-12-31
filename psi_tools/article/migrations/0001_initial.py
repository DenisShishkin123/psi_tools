# Generated by Django 4.2.7 on 2023-11-13 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(verbose_name='Контент')),
                ('image', models.ImageField(upload_to='image/%Y/%m/%d')),
                ('date_create', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Статья',
            },
        ),
    ]
