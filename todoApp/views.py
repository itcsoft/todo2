from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .models import Todo

# Получение данных из БД
def homepage(request):
    todos = Todo.objects.all()
    return  render(request, "index.html", {'todos':todos})

# Сохранение данных в БД
def create(request):
    if request.method == 'POST':
        todo = Todo()
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.save()
    return HttpResponseRedirect('/')

# Изменить данных в БД
def edit(request, id):
    try:
        todo = Todo.objects.get(id=id)
    
        if request.method == 'POST':
            todo.title = request.POST.get('title')
            todo.description = request.POST.get('description')
            todo.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, 'edit.html', {'todo':todo})
    except Todo.DoesNotExist:
        return HttpResponseNotFound("<h2>Todo not found</h2>")

# Удалить данных из БД
def delete(request, id):
    try:
        todo = Todo.objects.get(id=id)
        todo.delete()
        return HttpResponseRedirect('/')
    except Todo.DoesNotExist:
        return HttpResponseNotFound("<h2>Todo not found</h2>")