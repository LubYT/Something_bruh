from django.contrib import admin
from .models import Advertisements
# Register your models here.


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','price','created_at','updated_at','auction']
    list_filter = ['auction','created_at','updated_at']
    actions=['make_auction_as_false']
    fieldsets=(
        ('Общее',{
            'fields':('title','description')
        }),
        ('Финансы', {
            'fields':('price','auction')
        })
    )


    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self,request,queryset):
        queryset.update(auction=False)
admin.site.register(Advertisements, AdvertisementAdmin)