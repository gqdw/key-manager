from django.db import models

# Create your models here.

class Key(models.Model):
	name = models.CharField(max_length=30)
	public_key = models.TextField()

	def __unicode__(self):
		return self.name
class Host(models.Model):
	hostname = models.CharField(max_length=30)
	eth0_ip = models.GenericIPAddressField()
	eth1_ip = models.GenericIPAddressField()

	def __unicode__(self):
		return self.hostname


