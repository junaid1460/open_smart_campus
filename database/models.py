from django.db import models

# Create your models here.


#staffs
class Staff(models.Model):
    _first_name = models.CharField(max_length = 100)
    _last_name = models.CharField(max_length = 100)
    _date_of_birth = models.DateField()
    def __str__(self):
        return self._first_name + ", "+ self._last_name



#departments
class Department(models.Model):
    _name = models.CharField(max_length = 300, default = None)

#Academic years <- (department)
class AcademicYear(models.Model):
    _department = models.ForeignKey(Department, default = None )
    _year = models.IntegerField()
    _tag_name = models.CharField(max_length = 300)

#student Batches
class Batch(models.Model):
    _name = models.CharField(max_length = 300)
    _year = models.DateField()


    
#lecturer <- (staff & department)
class Lecturer(models.Model):
    _is = models.ForeignKey(Staff)
    _department =  models.ForeignKey(Department)

#period <- AcademicYear
class Period(models.Model):
    _academic_year = models.ForeignKey(AcademicYear)

#subjects <- (Department & Period)
class Subject(models.Model):
    _department = models.ForeignKey(Department)
    _period = models.ForeignKey(Period)

# SubjectAllotted <-(lecturer & subject & ...)
class SubjectAllotted(models.Model):
    _lecturer = models.ForeignKey(Lecturer)
    _subject = models.ForeignKey(Subject)



