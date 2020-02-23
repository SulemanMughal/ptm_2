from django.contrib import admin
from .models import properties,shortlist,notes,tourrequests,offers

admin.site.register(properties)
admin.site.register(shortlist)
admin.site.register(notes)
admin.site.register(tourrequests)
admin.site.register(offers)