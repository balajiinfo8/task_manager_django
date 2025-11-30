from django.urls import path 
from . import views 


# URL PATTERN IN APP 
urlpatterns = [
    path('',views.index,name="todo"),
    path('del/<int:item_id>',views.remove,name='del'),
    path('edit/<int:item_id>',views.index,name='edit'),

]