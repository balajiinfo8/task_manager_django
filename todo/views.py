from django.shortcuts import render , redirect
from django.contrib import messages
# Create your views here.
from .forms import TodoForm
from .models import Todo
from django.shortcuts import get_object_or_404
# login required
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate , login 
from django.contrib.auth import logout

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo')  # redirect to /home/
        else:
            messages.error(request, "Invalid username and password")

    # Always render login page (for GET or failed POST)
    return render(request, 'todo/login.html')


@login_required
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

def remove(request,item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request,"Item Removed...!")
    return redirect('todo')

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout