#Snippet Codes for Python
#Video 11

from datetime import datetime 
today = datetime.now()
month = str(raw_input('Please enter a month: '))
if month != today.strftime('%B'):
	print 'This month is not',month
elif month == 'October':
	print 'You write: ',month
else:
	print 'This month is: ',today.strftime('%B')
