from django.db import models
from django import forms
from .models import Card, MyCard

class MyCardForm(forms.ModelForm):
	class Meta:
		model = MyCard
		exclude = ['owner', 'card']

class NewCardForm(forms.Form):
	bulk_field = forms.CharField(widget=forms.Textarea, required=True)

	def clean_bulk_field(self):
		""" Checks if cards are formatted correctly and exist in the catalogue.
			ex. 170 NA
				Ruby NA
			Returns list of tuples i.e. [('Fang', 'NA'), ('Kabuki', 'EU')] """
		data = self.cleaned_data['bulk_field']
		cards = data.split('\r\n')
		fcards = [card.strip() for card in cards]

		for i in range(len(fcards)):
			fcard = fcards[i]
			info = fcard.split()
			
			if len(info) != 2:
				raise forms.ValidationError("{0} is not a valid format.".format(fcard))
			
			misc = info[0]
			version = info[1]
			exists = None

			if misc.isalpha():
				exists = Card.objects.filter(character=misc, version=version)
			else:
				exists = Card.objects.filter(number=misc, version=version)

			if not exists:
				raise forms.ValidationError("{0} is not a valid card.".format(fcard))

			fcards[i] = (exists.first().character, version)

		return fcards
