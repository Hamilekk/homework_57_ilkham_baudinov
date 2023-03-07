from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from webapp.forms import TaskForm


class AddTask(TemplateView):
    template_name = 'task_add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm()
        return context

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if not form.is_valid():
            return render(request, 'task_add.html', context={
                'form': form
            })
        else:
            task = form.save()
            return redirect('detail_view', pk=task.pk)