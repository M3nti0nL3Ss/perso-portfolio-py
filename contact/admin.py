from django.contrib import admin
from .models import Contact

class Contactt(admin.ModelAdmin):
	list_display = ['name','email','sent','message']
	list_filter = ['sent']
	readonly_fields = ["name","email","message"]

admin.site.register(Contact,Contactt)