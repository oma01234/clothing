from django.db import models
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)
    no_of_sub = models.IntegerField(default=0)
    cid = models.IntegerField(default=0)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name) + ' | ' + str(self.pk)
