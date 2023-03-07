from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=100, null=False)
    price = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    release_date = models.CharField(max_length=100)
    lte_exists = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, null=True)

    def __str__(self):
        return (f'{self.name}')