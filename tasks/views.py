from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views import View

'''
def task_list(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})
'''
# Clase con Form
'''
class TaskList(View):
    def get(self, request):
        form = TaskForm()
        tasks = Task.objects.all()
        return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})
    
    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            newTitle = form.cleaned_data['title']
            newDescription = form.cleaned_data['description']
            newCompleted = form.cleaned_data['completed']

            Task.objects.create(
                title=newTitle,
                description=newDescription,
                completed=newCompleted
            )

            return redirect('task_list')
        tasks = Task.objects.all()
        return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})
'''
# Uso de clase basada en vistas

class TaskList(View): # Vista para listar las tareas
    def get(self, request):
        tasks = Task.objects.all()
        return render(request, 'tasks/task_list.html', {'tasks': tasks})

class TaskDetail(View): # Vista para ver los detalles de una tarea
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        return render(request, 'tasks/task_details.html', {'task': task})

class TaskCreate(View): # Vista para crear una tarea
    def get(self, request):
        form = TaskForm()
        return render(request, 'tasks/task_create.html', {'form': form})
    
    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, 'tasks/task_create.html', {'form': form})

class TaskUpdate(View): # Vista para actualizar una tarea
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        form = TaskForm(instance=task)
        return render(request, 'tasks/task_update.html', {'form': form, 'task': task})
    
    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, 'tasks/task_update.html', {'form': form, 'task': task})