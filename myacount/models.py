from django.db import models

# Create your models here.
class User(models.Model):
    # --- int pk autoincrement
    id = models.AutoField(primary_key=True , db_column="ID")
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=12)
    email = models.EmailField(max_length=100 )
    activ = models.BooleanField()