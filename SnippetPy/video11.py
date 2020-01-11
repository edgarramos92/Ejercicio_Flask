#Snippet Codes for Python
#Video 11: If, then, else

from datetime import datetime 
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December','january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december')
today = datetime.now()
month = str(input('Please type a month name: '))
index = 0
for i in months:
	if month == i:
		print ('You type the month: ',month)
		index = 1
if index == 0:
	print('The month you type is misspelled!')
	
