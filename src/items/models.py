from django.db import models

# Create your models here.
class Item(models.Model):

    name = models.CharField(max_length=200)
    price = models.IntegerField()
    class Meta:
        db_table='items'