from django.db import models
from django.db.models.deletion import SET_NULL


# Create your models here.
class Machines(models.Model):
    machine_name=models.CharField(max_length=250)
    buy_date=models.DateField("fecha de compra",auto_now_add=True)
    marca=models.CharField(max_length=250)

class Devices(models.Model):
    machines=models.ForeignKey(Machines,on_delete=SET_NULL,null=True)
    device_name=models.CharField(max_length=250)
    sectret=models.CharField(max_length=250)

class Dots(models.Model):
    devices=models.ForeignKey(Devices,on_delete=SET_NULL,null=True)
    value=models.FloatField()
    units=models.CharField(max_length=250)




