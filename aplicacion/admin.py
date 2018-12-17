# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from aplicacion.models import vendedor, prenda, venta

class vendedorAdmin(admin.ModelAdmin):
	list_display = ('id',)
    	#prepopulated_fields = {'slug':('name',)}
	#admin.site.register(Category)


# Add in this class to customise the Admin Interface
class prendaAdmin(admin.ModelAdmin):
	list_display = ('id',)

# Add in this class to customise the Admin Interface
class ventaAdmin(admin.ModelAdmin):
	list_display = ('id',)

# Register your models here.
admin.site.register(vendedor, vendedorAdmin)
admin.site.register(prenda, prendaAdmin)
admin.site.register(venta, ventaAdmin)
