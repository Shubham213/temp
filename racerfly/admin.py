from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

## Category with Series
class SeriesInline(admin.TabularInline):
	model = Series

class CategoryAdmin(admin.ModelAdmin):
	inlines = [
		SeriesInline,
	]
admin.site.register(Category, CategoryAdmin)


## Series with Items
class ItemInline(admin.StackedInline):
	model = Item

class SeriesAdmin(admin.ModelAdmin):
	inlines = [
		ItemInline,
	]
admin.site.register(Series, SeriesAdmin)


## Items individually

admin.site.register(Item)

## Customers
admin.site.register(Customer)


admin.site.register(ItemCart)
admin.site.register(Cart)
admin.site.register(ItemToBuy)
admin.site.register(Order)
admin.site.register(FeedBack)


admin.site.register(Util)
admin.site.register(Coupon)
