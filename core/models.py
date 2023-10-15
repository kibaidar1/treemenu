from django.db import models


class MenuModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название меню')
    slug = models.SlugField(unique=True, verbose_name='Ссылка')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='child',
                               null=True, blank=True, verbose_name='Родитель')

    class Meta:
        unique_together = ('name', 'parent')

    def __str__(self):
        return self.name





