from django.db import models
from course.models import *
# from course.models import *

# Create your models here.

class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    # --- data coming from FK is object type not int -----
    course_id = models.ForeignKey('course.Course',on_delete=models.CASCADE) 