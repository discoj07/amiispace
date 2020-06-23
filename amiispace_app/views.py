from django.shortcuts import render
from django.http import HttpResponse

from amiispace_app.forms import MyCardForm

def index(request):
	form = MyCardForm(request.POST)
	context = {'form': form}
	return render(request, 'amiispace_app/index.html', context)
