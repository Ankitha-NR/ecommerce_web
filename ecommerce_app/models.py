# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class storetable(models.Model):
   id = models.AutoField(primary_key=True)
   store_name = models.CharField(max_length=30,default="N/A")
   store_location = models.CharField(max_length=50,default="N/A")
   store_owner_name = models.CharField(max_length=6,default='N/A')

   def save(self, *args, **kwargs):
       return super(storetable, self).save(*args, **kwargs)

   def __unicode__(self):
       return str(self.id)

   class Meta:
       db_table='store_table_1'
       app_label='ecommerce_app'