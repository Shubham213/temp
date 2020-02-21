from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .forms import *
from .models import *
from .decorators import customer_login_required
import random
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from Ecommerce.settings import EMAIL_HOST_USER, SENDGRID_API_KEY
from django.utils.html import strip_tags
import razorpay
import hmac, hashlib
import string
from decimal import Decimal
from racerfly.templatetags.tags import *
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
# Create your views here.

## UTILS
# dollarToRs = Util.objects.get(name='DollarToRs').float_value


########## TEST KEYS
# APP_ID = 'rzp_test_VTMvgmRWpMvYip'
# APP_SECRET = '399xvFLXfpeXjNpQ8B0W0wDU'

########## LIVE KEYS
APP_ID = 'rzp_live_46KNgnEVu2I48A'
APP_SECRET = 'Y8zoPpXjNyJimVmDvyvqvxwb'


razorpay_client = razorpay.Client(auth=(APP_ID, APP_SECRET))
# razorpay_client.set_app_details({"title" : "Racerfly", "version" : "2.0.2"})
# razorpay_client = razorpay.Client(auth=("<YOUR_API_KEY>", "<YOUR_API_SECRET>"))

def get_user(request):
	user = Customer.objects.get(id=request.session['user_id'])
	return user

def randomStringDigits(stringLength):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

def addPriceToCart(item, gst):

	return Decimal(float(item.item.priceDollar)*float((100-item.item.discount)/100)*float(item.quantity)*(1+gst/100))

def addToCart(request, item, qty, gst, special_requirements=None):
	
	user = get_user(request)

	# Create new ItemCart
	new_itemcart = ItemCart(
		item = item,
		quantity = int(qty),
		special_requirements = special_requirements,
	)
	new_itemcart.save()

	# print('\n\n' + str(addPriceToCart(new_itemcart, gst)) + '\n\n')

	# Update user cart
	if user.cart:
		user.cart.items.add(new_itemcart)
		user.cart.totPrice += addPriceToCart(new_itemcart, gst)# Decimal(float(new_itemcart.item.priceDollar)*float((100-new_itemcart.item.discount)/100)*float(new_itemcart.quantity)*(gst/100))
		user.cart.save()
		user.save()
	else:
		new_cart = Cart(totPrice=addPriceToCart(new_itemcart, gst))
		new_cart.save()
		new_cart.items.add(new_itemcart)
		user.cart = new_cart
		user.save()

def addToFav(request, item):
	user = get_user(request)
	user.favourites.add(item)
	user.save()

def sendMailSendGrid(request, to_email, subject, html_content):

	message = Mail(
	    from_email= 'RacerFly <sales@racerfly.com>',
	    to_emails=to_email,
	    subject=subject,
	    html_content=html_content)
	# print(message)
	try:
	    sg = SendGridAPIClient('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')
	    # sg = SendGridAPIClient(os.environ.get('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'))
	    response = sg.send(message)
	    # print(response.status_code)
	    # print(response.body)
	    # print(response.headers)
	except Exception as e:
	    print(str(e))

###### HOME

def home(request):
	categories = Category.objects.all()

	auth = False
	if ('user_id' in request.session) and Customer.objects.filter(id=request.session['user_id']).exists():
		auth = True
		user = get_user(request)
		return render(request, 'racerfly/home.html', {'auth': auth, 'user': user, 'categories': categories})
	elif ('user_id' in request.session) and (not Customer.objects.filter(id=request.session['user_id']).exists()):
		del request.session['user_id']
	return render(request, 'racerfly/home.html', {'auth': auth, 'categories': categories})

######### AUTHENTICATION

def ajax_generate_code(request):
	# print(request.GET)
	for x in request.GET:
		if x!='_':
			email = x

			## Generate Code and save it in a session
			request.session['code'] = random.randint(100000, 999999)
			# print(request.session['code'])

			## Send email Functionality
			html_content = render_to_string('racerfly/auth/verify_email.html', {'code': request.session['code']})
			sendMailSendGrid(request, email, 'Verify Email', html_content)

			# text_content = "Your Email Verification Code is " + str(request.session['code'])
			# msg = EmailMultiAlternatives('Verify Email', text_content, EMAIL_HOST_USER, [email])
			# msg.send()

			return HttpResponse("success")

def password_check(passwd): 
      
    SpecialSym =['$', '@', '#', '%'] 
    error = None
      
    if len(passwd) < 6: 
        error = 'length should be at least 6'
          
    if len(passwd) > 20: 
        error = 'length should be not be greater than 8'
          
    # if not any(char.isdigit() for char in passwd): 
    #     error = 'Password should have at least one numeral'
          
    # if not any(char.isupper() for char in passwd): 
    #     error = 'Password should have at least one uppercase letter'
          
    # if not any(char.islower() for char in passwd): 
    #     error = 'Password should have at least one lowercase letter'
          
    # if not any(char in SpecialSym for char in passwd): 
    #     error = 'Password should have at least one of the symbols $,@,#'

    if error:
    	return error

def register(request):
	categories = Category.objects.all()

	if request.method=='POST':
		if ('password' in request.POST) and ('confirm_password' in request.POST) and request.POST['password']!=request.POST['confirm_password']:
			error = "Passwords didn't match !"
			return render(request, 'racerfly/auth/register.html', {'categories': categories, 'error': error})
		if Customer.objects.filter(email=request.POST['email']).exists():
			error = "This email is already registered with us."
			return render(request, 'racerfly/auth/register.html', {'categories': categories, 'error': error})
		error = password_check(request.POST['password'])
		if error:
			return render(request, 'racerfly/auth/register.html', {'categories': categories, 'error': error})

		## Check Verification Code
		if (not 'code' in request.POST) or (not 'code' in request.session) or (not request.POST['code']==str(request.session['code'])):
			error = "Invalid Verification Code !"
			return render(request, 'racerfly/auth/register.html', {'categories': categories, 'error': error})


		t_password_hash = hashlib.sha256()
		t_password_hash.update((request.POST['password']).encode())
		new_user = Customer(
			name=request.POST['name'],
			email = request.POST['email'],
			phone_no = request.POST['phone_no'],
			city = request.POST['city'],
			password = t_password_hash.hexdigest(),
		)
		#new_user.password = str(hash(request.POST['password']))
		new_user.save()
		return redirect('racerfly:login')
	return render(request, 'racerfly/auth/register.html', {'categories': categories})

def login(request):
	categories = Category.objects.all()
	if 'user_id' in request.session:
		return redirect('racerfly:home')
	form = LoginForm()
	if request.method=='POST':
		t_password_hash = hashlib.sha256()
		t_password_hash.update((request.POST['password']).encode())
		if Customer.objects.filter(email=request.POST['email'], password=t_password_hash.hexdigest()).exists():
			user = Customer.objects.get(email=request.POST['email'])
		# else if Customer.objects.filter(phone_no=int(request.POST['email']), password=str(hash(request.POST['password']))).exists():
		# 	user = Customer.objects.get(phone_no=int(request.POST['email']), password=str(hash(request.POST['password'])))
			request.session['user_id'] = user.id
			if 'url_to_go' in request.session:
				return redirect(request.session['url_to_go'])
			return redirect('racerfly:home')
	return render(request, 'racerfly/auth/login.html', {'form': form, 'categories': categories})

def forgot_password_index(request):

	sent = None
	if request.method=='POST':
		if not Customer.objects.filter(email=request.POST['email']).exists():
			error = 'We could not find an account registered with this email.'
			return render(request, 'racerfly/auth/forgot_password_index.html', {'error': error})

		email = request.POST['email']
		request.session['forgot_password_user_id'] = Customer.objects.get(email=email).id
		html_content = render_to_string('racerfly/auth/forgot_password_mail_content.html')
		sendMailSendGrid(request, request.POST['email'], 'Reset Password', html_content)
		# text_content = strip_tags(html_content)
		# msg = EmailMultiAlternatives('reset password', text_content, EMAIL_HOST_USER, [request.POST['email']])
		# msg.attach_alternative(html_content, 'text/html')
		# msg.send()
		sent = True
	return render(request, 'racerfly/auth/forgot_password_index.html', {'sent': sent})

def reset_password(request):
	categories = Category.objects.all()
	success = False
	if request.method=='POST':
		error = password_check(request.POST['password'])
		if error:
			return render(request, 'racerfly/auth/reset_password.html', {'error': error})

		customer = Customer.objects.get(id=request.session['forgot_password_user_id'])
		t_password_hash = hashlib.sha256()
		t_password_hash.update((request.POST['password']).encode())
		customer.password = t_password_hash.hexdigest()
		customer.save()
		success = True
		del request.session['forgot_password_user_id']
	return render(request, 'racerfly/auth/reset_password.html', {'success': success})

@customer_login_required
def logout(request):
	categories = Category.objects.all()
	del request.session['user_id']
	if 'url_to_go' in request.session:
		del request.session['url_to_go']
	return redirect('racerfly:login')



######## CONTENTS
@customer_login_required
def dashboard(request):
	gst = Util.objects.get(name='GST').float_value
	categories = Category.objects.all()
	user = get_user(request)
	if request.method=='GET':
		if 'param' in request.GET:
			item = Item.objects.get(id=int(request.GET['param']))
			new_itemcart = ItemCart(
				item = item,
				quantity = 1
			)
			new_itemcart.save()

			if user.cart:
				user.cart.items.add(new_itemcart)
				user.cart.totPrice += addPriceToCart(new_itemcart, gst)
				user.cart.save()
				user.save()
			else:
				new_cart = Cart(totPrice=addPriceToCart(new_itemcart, gst))
				new_cart.save()
				new_cart.items.add(new_itemcart)
				user.cart = new_cart
				user.save()

	return render(request, 'racerfly/dashboard.html', {'user': user, 'categories': categories})


def solve0(t):
	if len(t.sort.split(','))>=1:
		return int(t.sort.split(',')[0])
	return 0

def solve1(t):
	if len(t.sort.split(','))==2:
		return int(t.sort.split(',')[1])
	return 0

#@customer_login_required
def series(request, category_id):
	gst = Util.objects.get(name='GST').float_value
	auth = False
	user = None
	if ('user_id' in request.session) and Customer.objects.filter(id=request.session['user_id']).exists():
		auth = True
		user = get_user(request)
	categories = Category.objects.all()
	category = Category.objects.get(id=category_id)
	series = category.choice_series.all()

	if request.method=='POST':
		if not 'user_id' in request.session:
			return redirect('racerfly:login')
		if 'addToCart' in request.POST:
			item = Item.objects.get(id=int(request.POST['addToCart']))
			addToCart(request, item, item.min_quantity, gst)
		elif 'addToFav' in request.POST:
			item = Item.objects.get(id=int(request.POST['addToFav']))
			addToFav(request, item)
	return render(request, 'racerfly/series.html', {'auth': auth, 'series': series, 'category': category, 'categories': categories, 'dollarToRs': Util.objects.get(name='DollarToRs').float_value, 'user': user})


#@customer_login_required
def items(request, category_id, series_id):
	user = None
	gst = Util.objects.get(name='GST').float_value
	auth = False
	if ('user_id' in request.session) and Customer.objects.filter(id=request.session['user_id']).exists():
		auth = True
		user = get_user(request)
	categories = Category.objects.all()
	category = Category.objects.get(id=category_id)
	ser = Series.objects.get(id=series_id)
	items = ser.choice_items.all()
	

	# Make this optional
	# If no second element in sort, make it default to be 0

	items = sorted(
		items, 
		key=lambda t: solve1(t)
	)


	items = sorted(
		items, 
		key=lambda t: solve0(t)
	)


	# for item in items:
		# print(str(item) + ' : ' + str(item.sort))

	if request.method=='POST':
		if not 'user_id' in request.session:
			return redirect('racerfly:login')
		if 'addToCart' in request.POST:
			item = Item.objects.get(id=int(request.POST['addToCart']))
			addToCart(request, item, item.min_quantity, gst)
		elif 'addToFav' in request.POST:
			item = Item.objects.get(id=int(request.POST['addToFav']))
			addToFav(request, item)

	return render(request, 'racerfly/items.html', {'user': user, 'auth': auth, 'category': category, 'ser': ser, 'items': items, 'categories': categories, 'dollarToRs': Util.objects.get(name='DollarToRs').float_value})




#@customer_login_required
def buyItem(request, category_id, series_id, item_id):
	user = None
	gst = Util.objects.get(name='GST').float_value
	auth = False
	if ('user_id' in request.session) and Customer.objects.filter(id=request.session['user_id']).exists():
		auth = True
		user = get_user(request)
	categories = Category.objects.all()
	#user = get_user(request)
	category = Category.objects.get(id=category_id)
	ser = Series.objects.get(id=series_id)
	item = Item.objects.get(id=item_id)

	if request.method=='POST':
		if 'user_id' in request.session:
			user = get_user(request)
			# print(request.POST)

			if ('add_cart' in request.POST) and ('quantity' in request.POST) and request.POST['quantity']:
				addToCart(request, item, int(request.POST['quantity']), gst, request.POST['special_requirements'])

			elif ('fav' in request.POST):
				addToFav(request, item)

		else:
			return redirect('racerfly:login')

	return render(request, 'racerfly/buyItem.html', {'user': user, 'auth': auth, 'category': category, 'ser': ser, 'item': item, 'categories': categories, 'dollarToRs': Util.objects.get(name='DollarToRs').float_value})


@customer_login_required
def cart(request):
	coupon_err=None
	coupon_discount=None
	categories = Category.objects.all()
	user = get_user(request)
	dollarToRs = Util.objects.get(name='DollarToRs').float_value
	gst = Util.objects.get(name='GST').float_value
	if user.cart:
		# order_amount = int(float(user.cart.totPrice)*dollarToRs*100)
		order_amount = int(roundTo2(grandTotal(user.cart.totPrice))*100)
		request.session['order_amount'] = order_amount
		# print(order_amount)
		# print('\n\norder amount : ' + str(order_amount) + '\n\n')

		# Check if any coupon is applied or not
		if (request.method=='POST') and ('coupon' in request.POST):
			# print(request.POST)
			if Coupon.objects.filter(expiry_date__gte=datetime.now(), expired=False, code=str(request.POST['coupon'])).exists():
				coupon = Coupon.objects.get(code=str(request.POST['coupon']))
				# order_amount is in paise, while the maxdiscount field is for Rs/-
				coupon_discount = min(int(order_amount*coupon.discount/100), int(coupon.maxdiscount*100))
				order_amount -= coupon_discount
				request.session['coupon_applied'] = coupon.id
				request.session['order_amount'] = order_amount
				#coupon.expired = True
				#coupon.save()
			else:
				coupon_err = "Please Enter a valid Coupon!"

		razorpay_order_id = None
		if order_amount >= 1:
			order_currency = 'INR'
			order_receipt = 'order_rcptid_11'
			notes = {'Shipping address': str(user.city)}   # OPTIONAL
			payment_data = {
				'amount': order_amount,
				'currency': order_currency,
				'receipt': order_receipt,
				'notes': notes,
				# 'payment_capture': 0,
			}
			new_order = razorpay_client.order.create(data=payment_data)
			razorpay_order_id = new_order['id']

		if request.method=='POST':
			# Delete an item
			if 'delete' in request.POST:
				item_cart = ItemCart.objects.get(id=int(request.POST['item_no']))
				priceToDeduct = addPriceToCart(item_cart, gst)# item_cart.item.priceDollar * item_cart.quantity * (1-item_cart.item.discount/100)
				user.cart.items.remove(item_cart)
				user.cart.totPrice -= priceToDeduct
				user.cart.save()
				user.save()
				item_cart.delete()
				return redirect('racerfly:cart')

		# emptyCart = True
		# if user.cart:
		# 	items = user.cart.items.all()
		# 	print(items)
		# 	print(items.count())
		# 	if not items.count()==0:
		# 		emptyCart = False
		# 		totPrice = 0.00
		# 		for item_cart in items:
		# 			totPrice += item_cart.item.

		return render(
			request, 
			'racerfly/cart.html', 
			{
				'coupon_err': coupon_err,
				'coupon_discount': coupon_discount,
				'user': user, 
				'gst': gst,
				'items': items, 
				'categories': categories, 
				'dollarToRs': dollarToRs,
				'order_amount': order_amount, 
				'razorpay_order_id': razorpay_order_id
			}
		)
	return render(
		request, 
		'racerfly/cart.html', 
		{
			'user': user, 
			'categories': categories, 
			'order_amount': 0, 
		}
	)
	
@customer_login_required
def verify_payment(request):
	categories = Category.objects.all()
	user = get_user(request)

	# print(request.POST)
	request.session['delivery_address'] = request.POST['delivery_address']
	PAYMENT_ID = request.POST['razorpay_payment_id']
	request.session['PAYMENT_ID'] = PAYMENT_ID
	ORDER_ID = request.POST['shopping_order_id']
	# PAYMENT_ID = request.POST['shopping_order_id']
	# AMOUNT = int(float(user.cart.totPrice)*(Util.objects.get(name='DollarToRs').float_value)*100) #request.POST['amount']


	## Generate Signature
	key = bytes(APP_SECRET, 'utf-8')
	msg = ORDER_ID + "|" + PAYMENT_ID
	msg = bytes(msg, 'utf-8')
	dig = hmac.new(key=key, msg=msg, digestmod=hashlib.sha256)
	generated_signature = dig.hexdigest()


	#generated_signature = hmac_sha256(ORDER_ID + "|" + PAYMENT_ID, APP_SECRET)
	# generated_signature = hmac.new(bstr(ORDER_ID + "|" + PAYMENT_ID), APP_SECRET, hashlib.sha256 )

	params_dict = {
	    'razorpay_order_id': ORDER_ID,
	    'razorpay_payment_id': PAYMENT_ID,
	    'razorpay_signature': generated_signature,
	}
	#razorpay_client.utility.verify_payment_signature(params_dict)
	# razorpay_client.payment.capture(ORDER_ID, AMOUNT)

	try:
		razorpay_client.utility.verify_payment_signature(params_dict)
		return redirect('racerfly:payment_success')
	except:
		return redirect('racerfly:payment_failure')


@customer_login_required
def payment_success(request):
	dollarToRs = Util.objects.get(name='DollarToRs').float_value
	categories = Category.objects.all()
	gst = Util.objects.get(name='GST').float_value
	t_user = get_user(request)

	totPrice = t_user.cart.totPrice
	delivery_charge = deliveryCharge(totPrice)
	gst_price = round(float(totPrice*int(dollarToRs))*(gst/100), 2)

	# If Coupon was applied, expire it
	if 'coupon_applied' in request.session:
		coupon = Coupon.objects.get(id=request.session['coupon_applied'])
		coupon.expired = True
		coupon.save()
		

	itemsToShow = []
	for item in t_user.cart.items.all():

		# Generate Order ID
		t_order_id = randomStringDigits(stringLength=10)
		while ItemToBuy.objects.filter(order_id=t_order_id).exists():
			t_order_id = randomStringDigits(stringLength=10)

		delivery_address = t_user.last_address
		if 'delivery_address' in request.session:
			# print('\n\noops\n\n')
			delivery_address = request.session['delivery_address']
			del request.session['delivery_address']

		t_user.last_address = delivery_address
		t_user.save()
		

		itemToBuy = ItemToBuy.objects.create(
			user = t_user,
			quantity = item.quantity,
			order_time = datetime.now(),
			order_id = t_order_id,
			item = item.item,
			delievery_at = delivery_address,
			payment_id = request.session['PAYMENT_ID'],
		)
		itemToBuy.save()
		t_user.cart.items.remove(item)
		t_user.cart.totPrice = 0
		t_user.cart.save()
		t_user.save()
		itemsToShow.append(itemToBuy)
	del request.session['PAYMENT_ID']
	# print('\n\nAll Done\n\n')

	grandTotal = request.session['order_amount']/100
	del request.session['order_amount']

	## Send email Functionality
	email = t_user.email
	html_content = render_to_string(
		'racerfly/order_placed_mail.html', 
		{
			'user': t_user, 
			'itemsToShow': itemsToShow, 
			'dollarToRs': int(dollarToRs), 
			'grandTotal': grandTotal,
			'gst_price': gst_price,
			'delivery_charge': delivery_charge
		}
	)
	sendMailSendGrid(request, email, 'Order Placed in Racerfly', html_content)
	# text_content = strip_tags(html_content)
	# msg = EmailMultiAlternatives('Order Placed in Racerfly', text_content, EMAIL_HOST_USER, [email])
	# msg.send()

	
	return render(request, 'racerfly/payment_success.html', {'itemsToShow': itemsToShow, 'dollarToRs': dollarToRs, 'user': t_user, 'grandTotal': grandTotal})
	# return redirect('racerfly:dashboard')

@customer_login_required
def payment_failure(request):
	categories = Category.objects.all()
	return render(request, 'racerfly/payment_failure.html', {})


## Track Package
@customer_login_required
def track_order(request):
	categories = Category.objects.all()
	user = get_user(request)
	# order = ItemToBuy.objects.get(id=int(order_id))
	if request.method=='GET':
		if 'search' in request.GET:
			order_id = request.GET['search']
			if not ItemToBuy.objects.filter(order_id__iexact=order_id, user=user).exists():
				return render(request, 'racerfly/track_order.html', {'error': 'Please Enter a Valid Order ID'})
			order = ItemToBuy.objects.get(order_id__iexact=order_id)
			return render(request, 'racerfly/track_order.html', {'order': order})
	return render(request, 'racerfly/track_order.html', {})

## Terms and Conditions
def tnc(request):
	return render(request, 'racerfly/tnc.html', {})

def aboutUs(request):
	return render(request, 'racerfly/about_us.html', {})

def privacy_policy(request):
	return render(request, 'racerfly/privacy_policy.html', {})

## Contact Us
def cont_us(request):
	categories = Category.objects.all()
	if request.method=='POST':
		## New Feedback
		FeedBack.objects.create(
			email=request.POST['feed_email'],
			phone = int(request.POST['feed_phone']),
			feedback = request.POST['feed_txt']
		)
		return render(request, 'racerfly/cont_us.html', {'thankyou': 'Thank you for your feedback !'})
	return render(request, 'racerfly/cont_us.html', {})

################# AJAX 

def ajax_add_to_cart(request):
	pass



###### ADD DATA

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as adminLogout

# def adminLogin(request):
# 	form = AdminLoginForm(req)
# 	return render(request, 'admin/login.html', {'form': form})

@login_required(login_url="/admin/login/")
def upload_file(request):
	if request.method=='POST':
		if 'upload' in request.POST:
			from add_data import add_data
			add_data(request.POST['modelname'], request.POST['seriesname'], int(request.POST['thread']))
		elif 'logout' in request.POST:
			# user = request.user
			adminLogout(request)
			return redirect('racerfly:upload_file')
	return render(request, 'racerfly/data_upload/upload_file.html', {})




## AJAX VIEWS

# def saveSuggestion(request, url):
# 	try:
# 		print(request.POST)
# 		Suggestion.objects.create(
# 			text = request.GET['text'],
# 			suggested_on = datetime.now(),
# 		)
# 		return redirect(url)
# 	except:
# 		return redirect('racerfly:home')



