from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^hello$', views.Hello, name = "hello"),
	url(r'^hello2$', views.Hello2, name = "hello2")
]