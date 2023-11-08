from django.urls import path
from .views import login_user, signup, homepage, logout, profile
app_name = "authentication"

urlpatterns = [
    path("", homepage, name="homepage"),
    path("login", login_user, name='login'),
    path('signup', signup, name='signup'),
    path("logout", logout, name='logout'),
    path("profile", profile, name="profile")
]
