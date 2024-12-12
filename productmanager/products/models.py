from django.db import models





class Product(models.Model):   
  name = models.CharField('Название товара', max_length=200)
  description = models.TextField('Описание товара','')
  price = models.FloatField('цена товара')
  created_at = models.DateTimeField('дата добавления товара')
  
