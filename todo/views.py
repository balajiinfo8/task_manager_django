from django.shortcuts import render , redirect
from django.contrib import messages
# Create your views here.
from .forms import TodoForm
from .models import Todo
from django.shortcuts import get_object_or_404

def index(request,item_id=None):
    item_list = Todo.objects.order_by('-date')
    if item_id:
        task = get_object_or_404(Todo,id=item_id)
        form = TodoForm(request.POST or None, instance=task)
        if request.method == 'POST' and form.is_valid():
            form.save()
            messages.success(request,"Item Updated")
            return redirect('todo')
    else:
        form = TodoForm(request.POST or None)
        if request.method == 'POST' and form.is_valid():
            form.save()
            messages.success(request,"Item Added!")
            return redirect('todo')

    pages = {
        "forms" : form,
        "list":item_list,
        "title":"TODO ITEM",
        'editing' : item_id
    }
    return render(request,'todo/index.html',pages)

    return redirect('todo')
def remove(request,item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request,"Item Removed...!")
    return redirect('todo')
