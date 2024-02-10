from django.views.generic import TemplateView

from .models import Service, Employee


class IndexView(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.filter(active=True).order_by('?')
        context['employees'] = Employee.objects.filter(active=True).order_by('?')
        return context