from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="todo"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path("edit/<int:item_id>/", views.index, name="edit"),
    path("remove/<int:item_id>/", views.remove, name="remove"),
]