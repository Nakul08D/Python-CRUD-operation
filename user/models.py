from django.db import models

#user name:Rohan
#user password:Rohan@4321


# Create your models here.
class Student(models.Model):
    sno=models.IntegerField(blank=True,null=True)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    language=models.CharField(max_length=20,default='')
    image=models.ImageField(upload_to='media/',default="",null=True,blank=True)

    def __str__(self):
        return self.fname
