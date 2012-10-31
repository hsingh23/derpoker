from pokeviewer.models import Poke
from django.template import Context, RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.db.models import Count


def home(request):
  pokers = Poke.objects.annotate(num_pokes=Count('poker'))


  return render_to_response(
    'home.html',
    {'pokers' : pokers },
    context_instance=RequestContext(request))
