
from django.urls import path
from .views import main_page,register_done_page,user_signup_page,log_in_page,log_out_page,user_page,payment_done_page,mypayment,control_page


urlpatterns = [

    path('',main_page,name = 'mainpage'),
    path('done/',register_done_page,name = 'done'),
    path('signup/',user_signup_page,name = 'signup'),
    path('login/',log_in_page,name ='login'),
    path('logout/',log_out_page,name ='logout'),
    path('user/',user_page,name = 'user_page'),
    path('payment/',payment_done_page,name = 'payment'),
    path('mypayment/',mypayment,name = 'mypayment'),
    path('control/',control_page,name = 'control' )

]
