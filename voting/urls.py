from django.urls import path
from voting import views

app_name="voting"

urlpatterns = [
    path('register/',views.register,name="registration"),
    path('user_login/',views.user_login,name="user_login"),
    path('cast_vote/',views.cast_vote,name="cast_vote"),
]
