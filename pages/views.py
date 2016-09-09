# coding: utf-8

from django.views import generic


# Create your views here.
class Home(generic.TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)

        return context