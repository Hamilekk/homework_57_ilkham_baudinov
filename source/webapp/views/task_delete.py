from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView

from webapp.models import Task


class DeleteView(TemplateView):
    template_name = 'task_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Task, pk=kwargs['pk'])
        context['types'] = context['task'].type.all()
        return context


class ConfirmDelete(View):

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Task, pk=kwargs['pk'])
        issue.delete()
        return redirect('index')
