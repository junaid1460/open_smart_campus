from django.db import models

# Create your models here.


#staffs
class Staff(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    date_of_birth = models.DateField()

#departments
class Department(models.Model):
    name = models.CharField(max_length = 300)

#Academic years
class AcademicYear(models.Model):
    year = models.IntegerField()
    tag_name = models.CharField(max_length = 300)

#student Batches
class Batch(models.Model):
    name = models.CharField(max_length = 300)
    year = models.DateField()
    