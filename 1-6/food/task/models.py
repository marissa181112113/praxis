from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields import IntegerField
from django.db.models.fields import DecimalField

# Create your models here.
# class Task(models.Model):
#     item = models.TextField(default='')
class makanan(models.Model):
    itemmakan = models.TextField(default='')
    jenismakan = models.CharField(max_length=200)
    jumlahmakan = models.IntegerField(default=0)
    hargamakan = models.IntegerField()

class minuman(models.Model):
    itemminum = models.TextField(default='')
    jenisminum = models.CharField(max_length=200)
    jumlahminum = models.IntegerField(default=0)
    hargaminum = models.IntegerField()

class pesanan(models.Model):
      makanan = models.ForeignKey(makanan, on_delete=models.CASCADE)
      minuman = models.ForeignKey(minuman, on_delete=models.CASCADE)
      jumlah_makanan = models.IntegerField(default=0)
      jumlah_minuman = models.IntegerField(default=0)
