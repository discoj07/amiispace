from django.shortcuts import render, redirect
from django.http import HttpResponse

from amiispace_app.forms import MyCardForm

def index(request):
	context = {}
	if request.method == "POST":
		form = MyCardForm(request.POST)
		if form.is_valid():
			return redirect('/amiispace_app/index')
		else:
			context['form'] = form
			render(request, 'amiispace_app/index.html', context)
	else:
		context['form'] = MyCardForm()
	return render(request, 'amiispace_app/index.html', context)