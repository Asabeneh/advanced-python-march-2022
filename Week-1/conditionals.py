""" a = 10
if a > 0:
	print(f'{a} is positive')
elif a == 0:
	print(f'{a} is zero')
else:
	print(f'{a} is negative') """

weather = input('What is the weather like? ').lower()
if weather == 'rainy' :
	print('Take your raincoat')
elif weather == 'cloudy':
	print('Be careful, the weather is cloud and it is hard to predict')
elif weather == 'snowy':
	print('It could be slippery')
elif weather == 'sunny':
		print('Go out freely, it just it a shiny day')
else:
	print('No one knows about the weather')
