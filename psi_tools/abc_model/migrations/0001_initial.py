# Generated by Django 4.2.7 on 2023-11-13 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emotion', models.CharField(max_length=100, unique=True, verbose_name='эмоция')),
            ],
            options={
                'verbose_name': 'Эмоция',
            },
        ),
        migrations.CreateModel(
            name='ABCmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activating', models.TextField(blank=True, verbose_name='событие')),
                ('beliefs', models.TextField(blank=True, verbose_name='оценка')),
                ('consequences', models.TextField(blank=True, verbose_name='реакция')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('emotions', models.ManyToManyField(to='abc_model.emotion')),
            ],
        ),
    ]
