from django.contrib import admin
from .models import Building, Visit, Path, Route
# Register your models here.
admin.site.register(Building)
admin.site.register(Visit)
admin.site.register(Path)
admin.site.register(Route)