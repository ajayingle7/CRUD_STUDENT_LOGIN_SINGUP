from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Student(models.Model):
    sid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    mno = PhoneNumberField()
    city = models.CharField(max_length=50, default='PUNE')

    def __str__(self):
        return f'{self.sid}--{self.fname}--{self.lname}--{self.mno}--{self.city}'


class Course(models.Model):
    cid = models.ManyToManyField(Student)
    cname = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.cid}--{self.cname}'