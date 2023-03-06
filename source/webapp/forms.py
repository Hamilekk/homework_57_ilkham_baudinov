from django import forms
from django.core.exceptions import ValidationError

from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'status', 'type')
        labels = {
            'title': 'Заголовок задачи',
            'description': 'Описание задачи',
            'status': 'Статус',
            'type': 'Тип'
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длиннее 2-ух символов')
        return title
