from django.db import models

# Create your models here.

class Business(models.Model):
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32, null=True, default="SA")

class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32, db_index=True)
    ip = models.GenericIPAddressField(protocol="IPV4", db_index=True)
    port = models.IntegerField()
    b = models.ForeignKey(to="Business", to_field="id", on_delete=models.CASCADE)

class Host_to_app(models.Model):
    hostj = models.ForeignKey(to="Host", to_field="nid", on_delete=models.CASCADE)
    busj = models.ForeignKey(to="Business", to_field="id", on_delete=models.CASCADE)
