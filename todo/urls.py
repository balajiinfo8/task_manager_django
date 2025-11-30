from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name="login"),       # root → login.html
    path('home/', views.index, name="todo"),        # /home → index.html
    path('logout/', views.logout_view, name="logout"),  # logout route
    path('del/<int:item_id>', views.remove, name='del'),
    path('edit/<int:item_id>', views.index, name='edit'),
]
