from django.db import models


class Article(models.Model):
    class Meta:
        verbose_name = "Статья"

    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    title = models.CharField(max_length=100)
    content = models.TextField(verbose_name="Контент")
    image = models.ImageField(upload_to="image/%Y/%m/%d")
    date_create = models.DateTimeField()





