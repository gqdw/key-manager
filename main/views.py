from django.shortcuts import render
from .models import Key,Host
# Create your views here.
def index(req):
	hosts = Host.objects.all()
	print Host.objects.count()
	print Host.objects.all()
	print '123'
	return render(req, 'index.html', {'hosts':hosts})
	
