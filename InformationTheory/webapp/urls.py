from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='webapp-home'),
	path('output1', views.huffman, name='webapp-output-1'),
	path('output2', views.RSA_encrypt, name='webapp-output-2'),
]