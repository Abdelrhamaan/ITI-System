from django.db import models
from trainee.models import *
# Create your models here.


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    # trainee_id = models.ForeignKey('trainee.Trainee',on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.id) + ' ' + self.name