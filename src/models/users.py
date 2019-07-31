from django.db import models

class Users(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=30,default="")
   email_id = models.CharField(max_length=50,default="")
   password = models.CharField(max_length=20,default="")
   salt     = models.CharField(max_length=18,default="")

   def save(self, *args, **kwargs):
       return super(Users, self).save(*args, **kwargs)

   def __unicode__(self):
       return str(self.id)

   class Meta:
       db_table='user_table'
       app_label='src'