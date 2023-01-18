from django.contrib import admin

# Register your models here.
from .models import Menu
from .models import Booking
from .models import MenuItem
from .models import Category


admin.site.register(Menu)
admin.site.register(Booking)
admin.site.register(MenuItem)
admin.site.register(Category)
