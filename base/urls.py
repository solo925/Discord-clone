from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('room/<str:pk>/',views.room,name="room"),
    path('profile/<str:pk>/',views.userProfile,name="user_profile"),
    
    path('create_room/',views.createRoom,name = 'createroom'),
    path('update_room/<str:pk>/',views.updateRoom,name = 'updateRoom'),
    path('delete_room/<str:pk>/',views.deleteRoom,name = 'deleteRoom'),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logUserout,name="logout"),
    path('register/',views.register,name="register"),
    path('delete_message/<str:pk>/',views.deleteMessage,name = 'deletemessage'),
    path('profile/<str:pk>/',views.userProfile,name="profile"),
    path('update-user/',views.updateUser,name="update-user"),
    path('topics/',views.topicsPage,name="topics"),
    path('activity/',views.activityPage,name="activity"),
    
    
]
 