from django.db import models

# Create your models here.

class Usergroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=50)
    ctime = models.DateTimeField(auto_now_add=True, null=True)
    uptime = models.DateTimeField(auto_now=True,null=True)

class Userinfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    user_group = models.ForeignKey("Usergroup", to_field='uid', on_delete=models.CASCADE, default=1)