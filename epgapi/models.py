from django.db import models

# Create your models here.

class context_info(models.Model):
    ctxname=models.CharField(max_length=30)
    vpnrd = models.CharField(max_length=30)
    ints = models.JSONField()


