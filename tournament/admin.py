from django.contrib import admin

from .models import Participant, Tournament


admin.site.register(Participant)
admin.site.register(Tournament)
