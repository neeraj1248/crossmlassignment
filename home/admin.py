from django.contrib import admin

# Register your models here.

from .models import Card

class CardAdmin(admin.ModelAdmin):
    list_display = ['id','type','priority','status','assignee']
admin.site.register(Card,CardAdmin)