from django.contrib import admin
from resume.models import Category, Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	list_display = ('name','url')

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)