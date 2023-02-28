from django.contrib import admin
from django import forms
from django.forms.widgets import *
from .models import *

class DontLog:
    def log_addition(self, *args):
        return

    def log_change(self, *args):
        return

    def log_deletion(self, *args):
        return

# admin.site.register(Menu)


class MenuForm(forms.ModelForm):
    model = Menu
    class Meta:
        field = '__all__'
        
@admin.register(Menu)
class MenuAdmin(DontLog, admin.ModelAdmin):
    form = MenuForm