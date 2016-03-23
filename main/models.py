from django.db import models

# Create your models here.

class Key(models.Model):
	name = models.CharField(max_length=30)
	public_key = models.TextField()

	def __unicode__(self):
		return self.name


class HostManager(models.Manager):
	def create_host(self, hostname, eth0, eth1):
		host = self.create(hostname=hostname, eth0_ip=eth0, eth1_ip=eth1)
		return host


class Host(models.Model):
	hostname = models.CharField(max_length=30)
	eth0_ip = models.GenericIPAddressField()
	eth1_ip = models.GenericIPAddressField()
	objects = HostManager()

	def __unicode__(self):
		return self.hostname

