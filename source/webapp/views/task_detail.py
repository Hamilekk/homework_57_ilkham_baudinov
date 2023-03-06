from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from webapp.models import Task


class DetailView(TemplateView):
    template_name = 'detail_task.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        context['types'] = context['task'].type.all()
        return context
