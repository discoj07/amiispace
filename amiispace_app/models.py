from django.conf import settings
from django.db import models

## A generic card. Think about this like a catalog of existing prints.
class Card(models.Model):
	character = models.CharField(max_length=10)
	series = models.CharField(max_length=5)
	version = models.CharField(max_length=5)

	def __str__(self):
		return "{0} {1} {2}".format(self.series, self.character, self.version)

## A card that a user currently owns.
class MyCard(models.Model):
	WA = 'WA'

	SERIES_CHOICES = [
		(1, '1'),
		(2, '2'),
		(3, '3'),
		(4, '4'),
		(WA, 'WA')
	]

	EU = 'EU'
	NA = 'NA'
	JPN = 'JPN'

	VER_CHOICES = [
		(EU, 'EU'),
		(NA, 'NA'),
		(JPN, 'JPN')
	]

	NEW = 'New'
	GOOD = 'Good'
	FAIR = 'Fair'
	POOR = 'Poor'

	QUALITY_CHOICES = [
		(NEW, 'New'),
		(GOOD, 'Good'),
		(FAIR, 'Fair'),
		(POOR, 'Poor')
	]

	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	card = models.ForeignKey(Card, on_delete=models.CASCADE)
	quality = models.CharField(max_length=5, choices=QUALITY_CHOICES, default=NEW)
	bought_price = models.PositiveIntegerField(blank=True)
	selling_price = models.PositiveIntegerField(blank=True)
