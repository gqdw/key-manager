from django.shortcuts import render
from django.http import HttpResponse
from .models import Key,Host
# Create your views here.
def index(req):
	hosts = Host.objects.all()
	# print Host.objects.count()
	return render(req, 'index.html', {'hosts':hosts})

def test2(req):
	hosts = Host.objects.all()
	# print Host.objects.count()
	return render(req, 'test2.html', {'hosts':hosts})
	
def read(req):
	with open('/tmp/ecs.cvs.csv','r') as f:
		for line in f:
			hostname, eth0 ,eth1 = line.split(',')[:]
			print hostname,eth0,eth1
			h = Host(hostname=hostname,eth0_ip=eth0,eth1_ip=eth1)
			h.save()
	
	return HttpResponse('ok')
