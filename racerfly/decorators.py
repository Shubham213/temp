from .models import Customer
from django.shortcuts import redirect

def customer_login_required(function):
	def wrapper(request, login_url='racerfly:login', *args, **kwargs):
		if not 'user_id' in request.session:
			request.session['url_to_go'] = request.get_full_path()
			return redirect(login_url)
		elif not Customer.objects.filter(id=request.session['user_id']).exists():
			del request.session['user_id']
			return redirect(login_url)
		else:
			return function(request, *args, **kwargs)
	return wrapper