from django.contrib import admin
from hello.models import Specs
# Register your models here.
class SpecsAdmin(admin.ModelAdmin):
	list_display = ['title']
	search_fields = ['title']
		

admin.site.register(Specs, SpecsAdmin)