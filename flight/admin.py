from django.contrib import admin

from .models import Aircraft, Seat, Route, Airport
admin.site.register(Aircraft)
admin.site.register(Seat)
admin.site.register(Route)
admin.site.register(Airport)