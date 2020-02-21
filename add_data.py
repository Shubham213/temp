from racerfly.models import *
import pandas as pd
# from Ecommerce.settings import dollarToRs
import os
from django.core.files import File
from decimal import Decimal
from os import walk
dollarToRs = int(Util.objects.get(name='DollarToRs').float_value)

def add_data(cat_name, filename, thread_no):
	thread_no = str(thread_no)
	root = 'Data'+thread_no+'/'
	cat = None
	if Category.objects.filter(name=cat_name).exists():
		cat = Category.objects.get(name=cat_name)
	else:
		cat = Category(name=cat_name)
		cat.save()
	ser = None
	if cat.choice_series.filter(name=filename).exists():
		ser = cat.choice_series.filter(name=filename)[0]
	else:
		ser = Series(name=filename, category=cat)
		ser.save()
	data = pd.read_csv(root+str(cat_name)+'/'+str(filename)+'/'+filename+'.csv')
	# print(len(data['Supplier Code']))
	for i in range(len(data['Supplier Code'])):
		new_item = Item(
			product_code = data['Product Code'][i],
			supplier_code = data['Supplier Code'][i],
			series = ser,
			name = data['Name'][i],
			subname = data['SubName'][i],
			priceDollar = Decimal(float(data['Price USD'][i])),
			priceRs = data['Price USD'][i]*dollarToRs,
			description = data['Description'][i],
			# discount = Decimal(float(data['Discount'][i])),
			# min_quantity = data['Minimum Order'][i]
		)
		new_item.discount = 0.00
		if (not str(data['Discount'][i]).strip()=='nan') and (not str(data['Discount'][i]).strip()==''):
			new_item.discount = Decimal(float(data['Discount'][i]))
			new_item.save()
		new_item.min_quantity = 1
		new_item.save()
		if (not str(data['Minimum Order'][i]).strip()=='nan') and (not str(data['Minimum Order'][i]).strip()==''):
			new_item.min_quantity = Decimal(float(data['Minimum Order'][i]))
			new_item.save()
		if (not str(data['Sort'][i]).strip()=='nan') and (not str(data['Sort'][i]).strip()==''):
			new_item.sort = str(data['Sort'][i])
			new_item.save()
		try:
			print('trying : ' + str(root+str(cat) +'/' + str(filename) +'/images/'+ str(data['Product Code'][i])+'.png'))
			try:
				new_item.image1.save(filename+'.png', File(open(root+str(cat) +'/' + str(filename) +'/images/'+ str(data['Product Code'][i])+'.png', 'rb')))
			except:
				try:
					new_item.image1.save(filename+'.jpg', File(open(root+str(cat) +'/' + str(filename) +'/images/'+ str(data['Product Code'][i])+'.jpg', 'rb')))
				except:
					new_item.image1.save(filename+'.svg', File(open(root+str(cat) +'/' + str(filename) +'/images/'+ str(data['Product Code'][i])+'.svg', 'rb')))

			new_item.save()
			# print('and done')
		except:
			f = []
			mypath = root+str(cat) +'/' + str(filename) +'/images/'+ str(data['Product Code'][i])+'/'
			print('mypath = ' + str(mypath) + '\n')
			for (_, _, filenames) in walk(mypath):
				f.extend(filenames)
				break

			for n_iter, f_name in enumerate(f):
				print(str(n_iter) + ' : ' + str(f_name))
				if n_iter==0:
					try:
						print('\n\n' + str(mypath+str(f_name))+'\n\n')
						new_item.image1.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
					except:
						try:
							new_item.image1.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.jpg', File(open(mypath+str(f_name), 'rb')))
						except:
							new_item.image1.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.svg', File(open(mypath+str(f_name), 'rb')))
				if n_iter==1:
					try:
						new_item.image2.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
					except:
						try:
							new_item.image2.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.jpg', File(open(mypath+str(f_name), 'rb')))
						except:
							new_item.image2.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.svg', File(open(mypath+str(f_name), 'rb')))
				if n_iter==2:
					try:
						new_item.image3.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
					except:
						try:
							new_item.image3.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.jpg', File(open(mypath+str(f_name), 'rb')))
						except:
							new_item.image3.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.svg', File(open(mypath+str(f_name), 'rb')))
					# new_item.image3.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
				if n_iter==3:
					try:
						new_item.image4.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
					except:
						try:
							new_item.image4.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.jpg', File(open(mypath+str(f_name), 'rb')))
						except:
							new_item.image4.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.svg', File(open(mypath+str(f_name), 'rb')))
					# new_item.image4.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
				if n_iter==4:
					try:
						new_item.image5.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
					except:
						try:
							new_item.image5.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.jpg', File(open(mypath+str(f_name), 'rb')))
						except:
							new_item.image5.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.svg', File(open(mypath+str(f_name), 'rb')))
					# new_item.image5.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
				if n_iter==5:
					try:
						new_item.image6.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
					except:
						try:
							new_item.image6.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.jpg', File(open(mypath+str(f_name), 'rb')))
						except:
							new_item.image6.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.svg', File(open(mypath+str(f_name), 'rb')))
					# new_item.image6.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
				if n_iter==6:
					try:
						new_item.image7.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
					except:
						try:
							new_item.image7.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.jpg', File(open(mypath+str(f_name), 'rb')))
						except:
							new_item.image7.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.svg', File(open(mypath+str(f_name), 'rb')))
					# new_item.image7.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
				if n_iter==7:
					try:
						new_item.image8.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
					except:
						try:
							new_item.image8.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.jpg', File(open(mypath+str(f_name), 'rb')))
						except:
							new_item.image8.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.svg', File(open(mypath+str(f_name), 'rb')))
					# new_item.image8.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
				if n_iter==8:
					try:
						new_item.image9.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
					except:
						try:
							new_item.image9.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.jpg', File(open(mypath+str(f_name), 'rb')))
						except:
							new_item.image9.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.svg', File(open(mypath+str(f_name), 'rb')))
					# new_item.image9.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
				if n_iter==9:
					try:
						new_item.image10.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
					except:
						try:
							new_item.image10.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.jpg', File(open(mypath+str(f_name), 'rb')))
						except:
							new_item.image10.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.svg', File(open(mypath+str(f_name), 'rb')))
					# new_item.image10.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
				if n_iter==10:
					try:
						new_item.image11.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
					except:
						try:
							new_item.image11.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.jpg', File(open(mypath+str(f_name), 'rb')))
						except:
							new_item.image11.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.svg', File(open(mypath+str(f_name), 'rb')))
					# new_item.image11.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
				if n_iter==11:
					try:
						new_item.image12.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
					except:
						try:
							new_item.image12.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.jpg', File(open(mypath+str(f_name), 'rb')))
						except:
							new_item.image12.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.svg', File(open(mypath+str(f_name), 'rb')))
					# new_item.image12.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
				if n_iter==12:
					try:
						new_item.image13.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
					except:
						try:
							new_item.image13.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.jpg', File(open(mypath+str(f_name), 'rb')))
						except:
							new_item.image13.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.svg', File(open(mypath+str(f_name), 'rb')))
					# new_item.image13.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
				if n_iter==13:
					try:
						new_item.image14.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
					except:
						try:
							new_item.image14.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.jpg', File(open(mypath+str(f_name), 'rb')))
						except:
							new_item.image14.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.svg', File(open(mypath+str(f_name), 'rb')))
					# new_item.image14.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
				if n_iter==14:
					try:
						new_item.image15.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
					except:
						try:
							new_item.image15.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.jpg', File(open(mypath+str(f_name), 'rb')))
						except:
							new_item.image15.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.svg', File(open(mypath+str(f_name), 'rb')))
					# new_item.image15.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
				if n_iter==15:
					try:
						new_item.image16.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
					except:
						try:
							new_item.image16.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.jpg', File(open(mypath+str(f_name), 'rb')))
						except:
							new_item.image16.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.svg', File(open(mypath+str(f_name), 'rb')))
					# new_item.image16.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
				if n_iter==16:
					try:
						new_item.image17.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
					except:
						try:
							new_item.image17.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.jpg', File(open(mypath+str(f_name), 'rb')))
						except:
							new_item.image17.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.svg', File(open(mypath+str(f_name), 'rb')))
					# new_item.image17.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
				if n_iter==17:
					try:
						new_item.image18.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
					except:
						try:
							new_item.image18.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.jpg', File(open(mypath+str(f_name), 'rb')))
						except:
							new_item.image18.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.svg', File(open(mypath+str(f_name), 'rb')))
					# new_item.image18.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
				if n_iter==18:
					try:
						new_item.image19.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
					except:
						try:
							new_item.image19.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.jpg', File(open(mypath+str(f_name), 'rb')))
						except:
							new_item.image19.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.svg', File(open(mypath+str(f_name), 'rb')))
					# new_item.image19.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
				if n_iter==19:
					try:
						new_item.image20.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
					except:
						try:
							new_item.image20.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.jpg', File(open(mypath+str(f_name), 'rb')))
						except:
							new_item.image20.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.svg', File(open(mypath+str(f_name), 'rb')))
					# new_item.image20.save(str(cat_name)+'_'+str(filename)+'_'+str(f_name)+'.png', File(open(mypath+str(f_name), 'rb')))
				new_item.save()
		

		print('added ' + str(i+1) + ' item...')
	print('\nAll Done\n\n')

def add_data_with_file(cat_name, f):
	cat = None
	if Category.objects.filter(name=cat_name).exists():
		cat = Category.objects.get(name=cat_name)
	else:
		cat = Category(name=cat_name)
		cat.save()
	ser = None
	if cat.choice_series.filter(name=filename).exists():
		ser = cat.choice_series.filter(name=filename)[0]
	else:
		ser = Series(name=filename, category=cat)
		ser.save()
	data = pd.read_csv(f)
	# print(len(data['Supplier Code']))
	for i in range(len(data['Supplier Code'])):
		new_item = Item(
			supplier_code = data['Supplier Code'][i],
			series = ser,
			name = data['Name'][i],
			subname = data['SubName'][i],
			priceDollar = Decimal(float(data['Price USD'][i])),
			priceRs = data['Price USD'][i]*dollarToRs,
			description = data['Description'][i],
			discount = Decimal(float(data['Discount'][i])),
			min_quantity = data['Minimum Order'][i]
		)
		new_item.image1.save(filename+'.png', File(open(root+'Images/'+str(i+1)+'.png', 'rb')))
		new_item.save()
		print('added ' + str(i+1) + ' item...')
	print('\nAll Done\n\n')

# add_data('Battery', 'Temp Battery')