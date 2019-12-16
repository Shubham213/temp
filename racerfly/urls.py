from django.urls import path
from . import views

app_name = 'racerfly'

urlpatterns = [
	path('', views.home, name='home'),

	## AUTHENTICATION
	path('ajax_generate_code/', views.ajax_generate_code, name='ajax_generate_code'),
	path('register/', views.register, name='register'),
	path('login/', views.login, name='login'),
	path('forgot_password_index/', views.forgot_password_index, name='forgot_password_index'),
	path('reset_password/', views.reset_password, name='reset_password'),
	path('logout/', views.logout, name='logout'),

	## CONTENTS
	path('tnc/', views.tnc, name='tnc'),
	path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
	path('aboutUs/', views.aboutUs, name='aboutUs'),
	path('contactus/', views.cont_us, name='cont_us'),
	path('category/<int:category_id>/', views.series, name='series'),
	path('category/<int:category_id>/<int:series_id>/', views.items, name='items'),
	path('category/<int:category_id>/<int:series_id>/<int:item_id>/', views.buyItem, name='buyItem'),

	## User account
	path('dashboard/', views.dashboard, name='dashboard'),
	path('track/', views.track_order, name='track_order'),
	path('cart/', views.cart, name='cart'),
	path('verify_payment/', views.verify_payment, name='verify_payment'),

	## Payments
	path('payment_success/', views.payment_success, name='payment_success'),
	path('payment_failure/', views.payment_failure, name='payment_failure'),


	### Upload Files
	path('upload_123/', views.upload_file, name='upload_file'),

	# path('saveSuggestion/<int:url>/', views.saveSuggestion, name='saveSuggestion'),
]