from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'SignIn'
urlpatterns = [

    # the home page which deals with user login
    path('', LoginView.as_view(template_name='SignIn/index.html'), name="login"),

    # signin page for new users
    path('signin/', views.signin, name="signin")
]
