from django.contrib import admin
from .models import Register

# Register your models here.
class RegModelForm(admin.ModelAdmin):
    list_display = ['FirstName','SecondName','Email','Password','ConfirmPassword','MobileNumber']

admin.site.register(Register,RegModelForm)
