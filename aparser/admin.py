from django.contrib import admin

# Register your models here.
from .models import News, Images, Links

admin.site.register(News)
admin.site.register(Images)
admin.site.register(Links)
