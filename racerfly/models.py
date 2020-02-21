from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=255)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

class Series(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='choice_series')
	name = models.CharField(max_length=255)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.category.name + self.name

class Item(models.Model):
	product_code = models.CharField(max_length=20, null=True, blank=True)
	supplier_code = models.CharField(max_length=500, null=True, blank=True)
	series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name='choice_items')
	name = models.CharField(max_length=255)
	subname = models.CharField(max_length=255)
	priceDollar = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
	priceRs = models.IntegerField(default=0)
	description = models.TextField()
	image1 = models.ImageField(null=True, blank=True)
	image2 = models.ImageField(null=True, blank=True)
	image3 = models.ImageField(null=True, blank=True)
	image4 = models.ImageField(null=True, blank=True)
	image5 = models.ImageField(null=True, blank=True)
	image6 = models.ImageField(null=True, blank=True)
	image7 = models.ImageField(null=True, blank=True)
	image8 = models.ImageField(null=True, blank=True)
	image9 = models.ImageField(null=True, blank=True)
	image10 = models.ImageField(null=True, blank=True)
	image11 = models.ImageField(null=True, blank=True)
	image12 = models.ImageField(null=True, blank=True)
	image13 = models.ImageField(null=True, blank=True)
	image14 = models.ImageField(null=True, blank=True)
	image15 = models.ImageField(null=True, blank=True)
	image16 = models.ImageField(null=True, blank=True)
	image17 = models.ImageField(null=True, blank=True)
	image18 = models.ImageField(null=True, blank=True)
	image19 = models.ImageField(null=True, blank=True)
	image20 = models.ImageField(null=True, blank=True)
	manual = models.FileField(null=True, blank=True)
	discount = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
	min_quantity = models.IntegerField() # min quantity must to buy
	sold_out = models.BooleanField(default=False)
	sort = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return self.name


## User
# Items in cart
class ItemCart(models.Model):
	item = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name='choice_items', null=True, blank=True)
	quantity = models.IntegerField(default=0)
	special_requirements = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.item.name + str(self.quantity)

# Every customer will have his/her own cart
class Cart(models.Model):
	items = models.ManyToManyField(ItemCart, related_name='choice_cart', null=True, blank=True)
	totPrice = models.DecimalField(default=0.0000, decimal_places=4, max_digits=20)

	def __str__(self):
		return str(self.totPrice) + " $"

class ItemToBuy(models.Model):
	user = models.ForeignKey('Customer', related_name='my_orders', on_delete=models.CASCADE, null=True)
	quantity = models.IntegerField(default=1)
	payment_id = models.CharField(max_length=100, null=True, blank=True)
	order_id = models.CharField(max_length=25, unique=True, null=True, blank=True)
	order_time = models.DateTimeField(default=datetime.now())
	item = models.ForeignKey(Item, related_name='choice_itemstobuy', on_delete=models.SET_NULL, null=True)
	track = models.TextField(null=True, blank=True)
	delivered = models.BooleanField(default=False)
	delivered_on = models.DateTimeField(null=True, blank=True)
	delievery_at = models.CharField(max_length=255)

	def __str__(self):
		return self.item.name

class Order(models.Model):
	items = models.ManyToManyField(ItemToBuy, related_name='choice_order', null=True, blank=True)


class Coupon(models.Model):
	code = models.CharField(max_length=6, unique=True)
	#user = models.ForeignKey('Customer', on_delete=models.SET_NULL, related_name='choice_coupons', null=True, blank=True)
	expiry_date = models.DateTimeField()
	discount = models.FloatField(default=20.0)
	maxdiscount = models.FloatField(default=4000.0)
	expired = models.BooleanField(default=False)
	def __str__(self):
		return str(self.code)

class Customer(models.Model):
	name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255, unique=True)
	password = models.CharField(max_length=10000)
	phone_no = models.IntegerField(null=True, blank=True)
	city = models.CharField(max_length=255)
	email_verified = models.BooleanField(default=False)
	phone_verified = models.BooleanField(default=False)
	orders = models.ManyToManyField(Order, related_name='choice_users', null=True, blank=True)
	cart = models.ForeignKey(Cart, related_name='choice_users', on_delete=models.SET_NULL, null=True, blank=True)
	favourites = models.ManyToManyField(Item, related_name='choice_users_fav', null=True, blank=True)
	last_address = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.email

class FeedBack(models.Model):
	email = models.EmailField()
	phone = models.IntegerField(null=True, blank=True)
	feedback = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.email


class Suggestion(models.Model):
	text = models.TextField()
	suggested_on = models.DateTimeField(default=datetime.now())

	def __str__(self):
		return str(self.suggested_on)


### ADMIN SITES
class Util(models.Model):
	name = models.CharField(max_length=50)
	float_value = models.FloatField(null=True, blank=True)
	string_value = models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.name
