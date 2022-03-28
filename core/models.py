from django.db import models
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_quantity = models.IntegerField('Quantity')

def __str__(self):
    return self.item_name
