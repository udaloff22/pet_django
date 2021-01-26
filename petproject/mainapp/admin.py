from django.forms import ModelChoiceField
from django.contrib import admin


from . models import *




class LaptopAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field == 'cathegory':
            return ModelChoiceField(db_field, request, **kwargs)




class SmartphoneAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field == 'cathegory':
            return ModelChoiceField(db_field, request, **kwargs)



admin.site.register(Cathegory)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
