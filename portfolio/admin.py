from django.contrib import admin
from .models import Project

class Projectt(admin.ModelAdmin):
    class Media:
        js = ('ckeditor/ckeditor-init.js','ckeditor/ckeditor/ckeditor.js','ckeditor/conf.js')

admin.site.register(Project,Projectt)

