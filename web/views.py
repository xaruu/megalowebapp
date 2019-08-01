from django.shortcuts import render, HttpResponse, Http404
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from .models import Episodio
from .sss import getlink
from django.views.decorators.csrf import csrf_exempt

class HomeView(ListView):
    model = Episodio
    template_name = "home.html"

class EpisodioDetailView(DetailView):
    model = Episodio
    template_name = "episodio.html"

    def get_context_data(self, **kwargs):
        context = super(EpisodioDetailView, self).get_context_data(**kwargs)
        context['link'] = getlink(Episodio.objects.get(slug=self.kwargs['slug']).video_url)
        return context

@csrf_exempt
def link_discover(request, index):
	
	model_index = Episodio.objects.get(id=index)
	link = getlink(model_index.video_url)
	return HttpResponse(link)


