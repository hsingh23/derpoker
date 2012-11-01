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
from pokeviewer.models import Poke
from django.template import Context, RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.db.models import Count
from derpoker.settings import MAX_POKES_SHOW


def home(request):
  pokers = Poke.objects.values('poker', 'poker_profile_link').annotate(num_pokes=Count('poker')).order_by('-num_pokes')[:MAX_POKES_SHOW]


  return render_to_response(
    'home.html',
    {'pokers' : pokers },
    context_instance=RequestContext(request))
