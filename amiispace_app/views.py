from django.shortcuts import render, redirect
from django.http import HttpResponse

from amiispace_app.forms import MyCardForm

def index(request):
	form = MyCardForm(request.POST or None)
	print(form.is_valid())
	print(form.errors)
	if form.is_valid():
		return redirect('/amiispace_app/index')
	else:
		form = MyCardForm(request.POST)
	context = {'form': form}
	return render(request, 'amiispace_app/index.html', context)
