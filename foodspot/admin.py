from django.contrib import admin
from foodspot.models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('get_category_title_display',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(SubCategory)
admin.site.register(Topping)
admin.site.register(Food)
admin.site.register(Offer)
