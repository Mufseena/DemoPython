from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import Todo_form
from .models import Task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.
class Task_list_view(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task'

class  Task_detail_view(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'

class Task_update_view(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ['name','priority','date']

    def get_success_url(self):
        return reverse_lazy('cbv_detail',kwargs={'pk':self.object.id})

class Task_delete_view(DeleteView) :
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbv_home')

def home(request):
    task = Task.objects.all()
    if request.method =='POST':
        name = request.POST.get('task')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        task1 = Task(name=name,priority=priority,date=date)
        task1.save();
    return render(request,"home.html",{'task':task})
def delete(request,task_id):
    task = Task.objects.get(id = task_id)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task = Task.objects.get(id=id)
    f = Todo_form(request.POST or None,instance = task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,"edit.html",{'task':task,'f':f})