from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    pic = models.ImageField()
    pic_name = models.TextField()

    def __str__(self):
        return self.name
