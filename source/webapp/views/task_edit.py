from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView

from webapp.forms import TaskForm
from webapp.models import Task


class UpdateView(TemplateView):
    template_name = 'task_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs['pk'])
        context['form'] = TaskForm(instance=context['task'])
        return context

    @staticmethod
    def post(request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('detail_view', pk=task.pk)
        return render(request, 'task_update.html', context={'form': form, 'task': task})
