from django.db import models

# Create your models here.
class book(models.Model):#书基表
    bid=models.AutoField(primary_key=True)
    bname=models.CharField(max_length=100,null=False)
    bauther=models.CharField(max_length=100,null=False)
    bprices=models.FloatField(null=False,default=0)
class user(models.Model):#用户和管理员表
    username=models.CharField(max_length=100,null=False)
    password=models.CharField(max_length=100,null=False)
    typeword=models.CharField(max_length=100,null=False,default="普通用户")
