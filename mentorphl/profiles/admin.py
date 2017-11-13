from django.contrib import admin
from .models import Mentor, Mentee, Organization


admin.site.register(Mentor)
admin.site.register(Mentee)
admin.site.register(Organization)
