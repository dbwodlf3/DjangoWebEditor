from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'$', Main.as_view())
]
