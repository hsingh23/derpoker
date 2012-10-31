from pokeviewer.models import Poke
from django.contrib import admin


class PokeAdmin(admin.ModelAdmin):
  list_display = ('poker', 'poke_time', 'poker_profile_link',)
  list_filter = ('poker',)

admin.site.register(Poke, PokeAdmin)
