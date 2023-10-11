from django import forms
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from project_management.models import Task, Project, User


@login_required(login_url='login')
def index(request):
    context = dict(
        title='Project Management',
    )
    return render(request, 'project_management/pages/index.html', context=context)


@login_required(login_url='login')
def project_list(request):
    user = User.objects.first()  # it will be changed later
    items_per_page = 10
    my_project = Project.objects.filter(user=user)

    paginator = Paginator(my_project, items_per_page)
    page_number = request.GET.get('page')
    if not page_number:
        page_number = 1
    return render(request, 'project_management/pages/project_list.html', context=dict(
        title='Project Management',
        user_project=paginator.get_page(page_number),
        page=page_number,
    ))


@login_required(login_url='login')
def project_task(request, pk):
    project = Project.objects.get(id=pk)
    all_task = Task.objects.filter(project=pk)

    return render(request, 'project_management/pages/project_task.html', context=dict(
        title=f'{project.title}',
        pk=pk,
        all_task=all_task,
    ))


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'start', 'end', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.NumberInput(attrs={'class': 'form-control'}),
        }


def create_task(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            task = Task.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                start=form.cleaned_data['start'],
                end=form.cleaned_data['end'],
                status=form.cleaned_data['status'],
                project=project
            )
            task.save()
            return redirect('project_task', pk=pk)
    else:
        form = TaskCreateForm()

    return render(request, 'project_management/pages/create_task.html', context=dict(
        title='Create Task',
        form=form,
    ))


@login_required(login_url='login')
def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    return render(request, 'project_management/pages/task_detail.html', context=dict(
        title='Task Detail',
        task=task,
    ))


def create_project(request):
    return render(request, 'project_management/pages/create_project.html', context=dict())
