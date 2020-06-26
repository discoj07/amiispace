from django.db import models
from django import forms
from .models import Card, MyCard

class MyCardForm(forms.ModelForm):
	bulk_field = forms.CharField(widget=forms.Textarea, required=True)
	
	class Meta:
		model = MyCard
		exclude = ['owner', 'card', 'quality', 'bought_price', 'selling_price']

	def clean_bulk_field(self):
		""" Checks if cards are formatted correctly and exist in the catalogue. 
			ex. 170 NA
				Ruby NA
			Returns list of formatted cards. """
		cards = self.cleaned_data['bulk_field'].split('\r\n')
		formatted_cards = [card.strip() for card in cards]
		for card in formatted_cards:
			data = card.split()
			if len(data) != 2:
				raise forms.ValidationError("{0} is not a valid format.".format(card))
			misc = data[0]
			version = data[1]
			exists = None
			if misc.isalpha():
				exists = Card.objects.filter(character=misc, version=version)
			else:
				exists = Card.objects.filter(number=misc, version=version)
			if not exists:
				raise forms.ValidationError("{0} is not a valid card.".format(card))
		print(formatted_cards)
		return formatted_cards
