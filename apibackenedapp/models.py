from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token


# Create your models here.
#create a receiver for the signal 'post_save' for the user model 
#once its created create a token for that model

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)
    

#create class Department model class by inheriting the model class
class Department(models.Model):
    #dept id is auto incrementing and is the primary key
    DepartmentId = models.AutoField(primary_key=True)
    #dept name is a char field with max char length of 200
    DepartmentName = models.CharField(max_length=200)

    #whenever we try to print the dept object,
 #instead of the memory address of the object,
 #we need to return the name of the department

    def str(self):
        return self.DepartmentName

class Employee(models.Model):

 #emp id is auto incrementing and is the primary key
    EmployeeId = models.AutoField(primary_key=True)
    #emp name is a char field with max char length of 200
    EmployeeName = models.CharField(max_length=200)
    Designation = models.CharField( max_length=150)
    DateOfJoining = models.DateField()
#depid is a foreigh  key from the dept model
   
    DepartmentId = models.ForeignKey(Department,on_delete=models.CASCADE)
    Contact = models.CharField(max_length=150)
    IsActive = models.BooleanField(default=True)
    def _str_(self):
        return self.EmployeeName