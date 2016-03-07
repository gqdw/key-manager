from django.db import models

# Create your models here.

class Key(models.Model):
	name = models.CharField(max_length=30)
	public_key = models.CharField(max_length=300)

