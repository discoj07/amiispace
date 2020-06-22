from django.db import models
from django import forms
from .models import Card, MyCard

class MyCardForm(forms.ModelForm):
	bulk_field = forms.TextField(label='Bulk Field', required=True)

	class Meta:
		model = MyCard
		fields = [bulk_field]
