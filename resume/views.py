from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

# Create your views here.

def index(request):
	context = RequestContext(request)
	context_dict = {'boldmessage':'In Development phase'}
	return render_to_response('resume/index.html',context_dict,context)