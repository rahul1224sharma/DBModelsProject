from django.db import models

# Create your models here.
class Employee(models.Model):
        eno=models.IntegerField();
        ename=models.CharField(max_length=55);
        esal=models.FloatField();
        eaddr=models.CharField(max_length=30);
        def __str__(self):
                return str(self.eno)+self.ename+str(self.esal)+self.eaddr;


class Company(models.Model):
        compid=models.IntegerField()
        compname=models.CharField(max_length=60)
        noofemps=models.IntegerField()
        compaddr=models.CharField(max_length=50)
        compshare=models.FloatField();
        def __str__(self):
                return 'company object with compid:'+str(self.compid);
