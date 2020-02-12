from django import template
from racerfly.models import Util

#(Util.objects.get(name='DollarToRs').float_value) = Util.objects.get(name='DollarToRs').float_value
register = template.Library()

#(Util.objects.get(name='DollarToRs').float_value) = 70

@register.filter
def multiply(price, quantity):
	return float(price)*float(quantity)

@register.filter
def makediscount(price, discount):
	return round(float(price)*float((1-discount/100)), 2)

@register.filter
def roundTo2(val):
	return round(float(val), 2)

@register.filter
def toInt(val):
	return int(val)

@register.filter
def deliveryCharge(price):
	priceRs = float(price)*float(Util.objects.get(name='DollarToRs').float_value)
	if priceRs<400:
		return 70
	elif priceRs>401 and priceRs<1000:
		return 100
	elif priceRs>1001 and priceRs<3000:
		return 200
	elif priceRs>3001:# and priceRs<7000:
		return 500

@register.filter
def grandTotal(price):
	priceRs = float(price)*float(Util.objects.get(name='DollarToRs').float_value)
	return deliveryCharge(price)+priceRs



def solve0(t):
	if len(t.sort.split(','))>=1:
		return int(t.sort.split(',')[0])
	return 0

def solve1(t):
	if len(t.sort.split(','))==2:
		return int(t.sort.split(',')[1])
	return 0
	
@register.filter
def sortAndSlice(items, x):
	items = sorted(
		items, 
		key=lambda t: solve1(t)
	)
	items = sorted(
		items, 
		key=lambda t: solve0(t)
	)
	return items[:x]
