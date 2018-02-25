from django.shortcuts import render
from django.http import HttpResponse

from minConflict.algorithm import *

# Create your views here.

def api(request):

	result = my_custom_sql()

	print(result)

	return HttpResponse(result)
