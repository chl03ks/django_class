from django.contrib import admin

from .models import Coach, Team, Player
# Register your models here.

admin.site.register(Coach)
admin.site.register(Team)
admin.site.register(Player)
