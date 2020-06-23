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
