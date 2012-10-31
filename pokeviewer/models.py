from django.db import models

class Poke(models.Model):
  poker = models.CharField(max_length=200)
  poke_time = models.DateTimeField(auto_now_add=True)
  poker_profile_link = models.CharField(max_length=300)
