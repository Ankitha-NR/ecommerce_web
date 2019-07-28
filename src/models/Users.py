from django.db import models

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
       db_table='store_table'
       app_label='src'