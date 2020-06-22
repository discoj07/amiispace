from amiispace_app.models import Card

# Paste this into the shell to populate the Card database (assuming nothing is in the database).
# WARNING: Does NOT update pre-existing Card objects.

file = open("cards.txt", "r")
lines = file.readlines()

versions = ['EU', 'NA', 'JPN']

for i in range(0, len(lines) - 1):
	l = lines[i]
	line = l.replace('\n', '')
	formatted = line.split('\t')
	number = formatted[0]
	series = None

	if len(number) == 3:
		if int(number) % 100 == 0:
			series = "{0}".format(int(number[0]))
		else:
			series = "{0}".format(int(number[0]) + 1)
	elif number[0] is 'S':
		series = 'Sanrio'
	else: 
		series = 'WA'

	chara = formatted[1]

	for ver in versions:
		if series is 'Sanrio' and ver is 'NA':
			continue
		card = Card(character=chara, series=series, number=number, version=ver)
		card.save()