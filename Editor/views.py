from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

class Main(View):
	def get(self, request, *args, **kwargs):
		return HttpResponse("Well Come.")

	def post(self, request, *args, **kwargs):
		return HttpResponse("Get Out Here.")