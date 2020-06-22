from amiispace_app.models import Card

# Paste this entire file into the shell to update the Card database.

file = open("cards.txt", "r")
lines = file.readlines()

versions = ['EU', 'NA', 'JPN']

for i in range(0, len(lines) - 1):
	l = lines[i]
	line = l.replace('\n', '')
	formatted = line.split('\t')
	series = formatted[0]
	chara = formatted[1]
	for ver in versions:
		card = Card(character=chara, series=series, version=ver)
		card.save()
