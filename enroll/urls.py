from django.urls import path,include
from . import views
urlpatterns = [
    
    path('', views.home.as_view() , name="home"),
    path('signup/', views.user_signup, name="signup"),
    path('logout/', views.user_logout, name="logout"),
    path('login/', views.user_login, name="login"),
    path('<int:my_id>/', views.update_data.as_view(), name="updatedata"),
    path('delete/<int:my_id>/',views.delete_data.as_view(), name='deletedata'),
   
   
    
    
]