#
# Copyright 2012 Kurtis L. Nusbaum
#
# This file is part of derpoker.
#
# derpoker is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# derpoker is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with derpoker.  If not, see <http://www.gnu.org/licenses/>.
#
from django.db import models

class Poke(models.Model):
  poker = models.CharField(max_length=200)
  poke_time = models.DateTimeField(auto_now_add=True)
  poker_profile_link = models.CharField(max_length=300)
