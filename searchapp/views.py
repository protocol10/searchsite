from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.db.models import Q
from django.template import RequestContext
from django.core.context_processors import csrf
from models import Contact
import logging

logger=logging.getLogger(__name__)
# Create your views here.
def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def result(request):
	if request.method=='POST':
		name = request.POST['q']
		if name is  None:
			print name
			result=Contact.objects.all()
		else:
			#print name
			result = Contact.objects.filter(Q(name__contains=name))
			print result
	return render_to_response('results.html',{'result':result},context_instance=RequestContext(request))
	
