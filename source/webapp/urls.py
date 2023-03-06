from django.urls import path

from webapp.views.base import IndexView
from webapp.views.task_add import AddTask
from webapp.views.task_delete import DeleteView, ConfirmDelete
from webapp.views.task_detail import DetailView
from webapp.views.task_edit import UpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/id=<int:pk>/', DetailView.as_view(), name='detail_view'),
    path('tasks/add', AddTask.as_view(), name='task_add'),
    path('task/id=<int:pk>/update/', UpdateView.as_view(), name='task_update'),
    path('task/id=<int:pk>/', DeleteView.as_view(), name='task_delete'),
    path('task/id=<int:pk>/confirm_delete/', ConfirmDelete.as_view(), name='task_confirm_delete')
]
