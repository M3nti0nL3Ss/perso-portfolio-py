from django.contrib import admin
from .models import Blog
from django.utils.translation import ugettext_lazy


admin.site.site_title = ugettext_lazy("Hebbaj")
admin.site.site_header = ugettext_lazy("Portfolio Administration")
admin.site.index_title = ugettext_lazy("Index")


class Blogg(admin.ModelAdmin):
	list_display = ['title','date']
	list_filter = ['date']
	search_fields = ('title', 'description')
	prepopulated_fields = {'slug': ('title',)}
	class Media:
		js = ('ckeditor/ckeditor-init.js','ckeditor/ckeditor/ckeditor.js','ckeditor/conf.js')
admin.site.register(Blog,Blogg)
