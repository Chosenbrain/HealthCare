from django.contrib import admin
from .models import Blog,Category,Lab,Pricing,Pricingservice

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Lab)



class PricingserviceAdmin(admin.StackedInline):
    model = Pricingservice

@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    inlines = [PricingserviceAdmin]

    class Meta:
       model = Pricing

