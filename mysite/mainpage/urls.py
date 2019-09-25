
from django.urls import path
from .views import main_page,register_done_page

urlpatterns = [

    path('',main_page,name = 'mainpage'),
    path('done/',register_done_page,name = 'done')
]
