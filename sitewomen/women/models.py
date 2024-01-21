from django.db import models
from django.db import models
from django.urls import reverse


class Items(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    price = models.CharField(max_length=100, default='')
    weight = models.CharField(max_length=100, default='')
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)


    class Meta:

        verbose_name = "Товары"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('women:post', kwargs={'post_slug':self.slug})


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:

        verbose_name = "Категории"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('women:category', kwargs={'cat_slug':self.slug})