
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from .forms import TodoForm , RegistrationForm
from .models import Todo


def login_view(request):
    if request.user.is_authenticated:
        return redirect("todo")

    if request.method == "POST":
        identifier = request.POST.get("username","").strip()
        password = request.POST.get("password","")

        User = get_user_model()

        account = User.objects.filter(
            email__iexact=identifier
        ).first()

        username = account.username if account else identifier

        user = authenticate(
            request,
            username = username,
            password =  password,
        )

        if user is not None:
            login(request,user)
            return redirect("todo")
        messages.error(
            request,
            "Invalid username/email or password."
        )


    return render(request, "todo/login.html")


def register(request):
    if request.user.is_authenticated:
        return redirect("todo")

    form = RegistrationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Your account has been created successfully!")
        return redirect("login")

    return render(request, "todo/register.html", {"form": form})


@login_required
def index(request, item_id=None):
    # Only show tasks belonging to the logged-in user.
    item_list = Todo.objects.filter(owner=request.user).order_by("-date")

    if item_id is not None:
        task = get_object_or_404(
            Todo,
            id=item_id,
            owner=request.user,
        )
        form = TodoForm(request.POST or None, instance=task)

        if request.method == "POST" and form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            messages.success(request, "Item updated.")
            return redirect("todo")

    else:
        form = TodoForm(request.POST or None)

        if request.method == "POST" and form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            messages.success(request, "Item added.")
            return redirect("todo")

    pages = {
        "forms": form,
        "list": item_list,
        "title": "TaskForge",
        "editing": item_id,
    }

    return render(request, "todo/index.html", pages)


@login_required
@require_POST
def remove(request, item_id):
    task = get_object_or_404(
        Todo,
        id=item_id,
        owner=request.user,
    )
    task.delete()
    messages.info(request, "Item removed.")
    return redirect("todo")


@login_required
def logout_view(request):
    logout(request)
    return redirect("login")
