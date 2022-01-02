from django.shortcuts import redirect, render
from .forms import ProjectForm
from .models import Project
from django.urls import reverse

def projects(request):
    projects = Project.objects.all()
    context = {
        'title': 'Projects',
        'projects': projects
    }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project_object = Project.objects.get(id=pk)
    if project_object:
        reviews = project_object.review_set.all()
        context = {
            'project_object': project_object,
            'reviews': reviews,
        }
    return render(request, 'projects/single_project.html', context)

def create_project(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects_page')

    context = {'title': 'Create Project', 'form': form}
    return render(request, 'projects/project_form.html', context)

def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/projects/projects.html')
            
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)

def delete_project(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == 'POST':
        project.delete()
        return redirect('/projects/projects.html')

    return render(request, 'projects/delete.html', {'project': project})


project_list = [
    {
        'id': 1,
        'title': 'Ecommerce Website',
        'description': 'Full funtional ecommerce website',
    },
    {
        'id': 2,
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display works',
    },
    {
        'id': 3,
        'title': 'Social Nwtwork',
        'description': 'An open source project built community',
    },
]