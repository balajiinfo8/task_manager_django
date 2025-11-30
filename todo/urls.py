from django.urls import path
from . import views

urlpatterns = [
    # Root URL now shows login.html
    path('', views.login_view, name="login"),

    # Homepage moved to /home/
    path('home/', views.index, name="todo"),

    # Other routes
    path('del/<int:item_id>', views.remove, name='del'),
    path('edit/<int:item_id>', views.index, name='edit'),
]
