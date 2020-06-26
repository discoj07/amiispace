from django.shortcuts import render, redirect
from django.http import HttpResponse

from amiispace_app.forms import MyCardForm
from amiispace_app.models import MyCard, Card

def index(request):
	context = {}
	if request.method == "POST":
		form = MyCardForm(request.POST)
		if form.is_valid():
			for tup in form.cleaned_data['bulk_field']:
				character = tup[0]
				version = tup[1]
				query = Card.objects.filter(character=character, version=version)
				card = query[0]
				print(card)
				# create MyCard object but need user
			return redirect('/amiispace_app/index')
		else:
			context['form'] = form
			render(request, 'amiispace_app/index.html', context)
	else:
		context['form'] = MyCardForm()
	return render(request, 'amiispace_app/index.html', context)