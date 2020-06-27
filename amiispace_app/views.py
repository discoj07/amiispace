from django.contrib.auth import get_user_model 
from django.shortcuts import render, redirect

from amiispace_app.forms import MyCardForm, NewCardForm
from amiispace_app.models import MyCard, Card

def index(request):
	""" Add cards view. """
	context = {}
	if request.method == 'POST':
		form = NewCardForm(request.POST)
		if form.is_valid():
			user = get_user_model().objects.first()
			cards = form.cleaned_data['bulk_field']
			for card in cards:
				character = card[0]
				version = card[1]
				query = Card.objects.filter(character=character, version=version)
				my_card = MyCard(owner=user, card = query.first())
				my_card.save()
				return redirect('/amiispace_app/index')
		else:
			context['form'] = form
			return render(request, 'amiispace_app/index.html', context)
	else:
		form = NewCardForm()
		context['form'] = form
	return render(request, 'amiispace_app/index.html', context)
