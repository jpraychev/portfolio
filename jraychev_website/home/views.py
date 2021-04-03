from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, RedirectView

# class IndexView(TemplateView):
    # template_name  = 'home/index.html'

class IndexView(RedirectView):

    permanent = False
    pattern_name = 'about'

    def get_redirect_url(self, *args, **kwargs):
        return super().get_redirect_url(*args, **kwargs)