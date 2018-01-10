from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

class Main(View):
	template_name = 'editor/layout.html'
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

	def post(self, request, *args, **kwargs):
		return HttpResponse("Get Out Here.")