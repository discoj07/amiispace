from django.db import models
from django import forms
from .models import Card, MyCard

class MyCardForm(forms.ModelForm):
	bulk_field = forms.CharField(widget=forms.Textarea, required=True)
	
	class Meta:
		model = MyCard
		exclude = ('owner', 
			'card',
			'quality',
			'bought_price',
			'selling_price')

	def to_python(self, value):
		""" Normalize data to a list of strings. """
		print("to_python")
		if not value:
			return []
		print(value.split())
		return value.split()

	def validate(self, value):
		""" Check if value consists only of valid cards. """
		print("validate")
		super().validate(value)
		for card in value:
			print(card)
			validate_card(card)

	def validate_card(self, card):
		""" Check if card is a valid card. 
			ex. 170 NA """
		print("validate_card")
		formatted = card.split()
		l = len(formatted)
		
		if l != 2:
			raise forms.ValidationError("{0} is not a valid input.".format(card))

		number = formatted[0]
		version = formatted[1]
		valid = Card.objects.get(number=number, version=version)

		if valid:
			raise forms.ValidationError("{0} is not a valid card.".format(card))
		else:
			return
