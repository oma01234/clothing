from django.db import models

# Create your models here.


class SubCat(models.Model):
    item_name = models.CharField(max_length=30)
    item_price = models.IntegerField()
    item_pic = models.ImageField()
    pic_name = models.TextField()
    catid = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item_name
