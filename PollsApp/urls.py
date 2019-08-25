from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.http import HttpResponse
from django.contrib.auth.views import LogoutView

app_name = 'PollsApp'
urlpatterns = [

    # basic urls
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(), name="logout"),
    url(r'^oauth/', include('social_django.urls', namespace="social")),
    url(r'^', include('django.contrib.auth.urls')),

    # to the SignIn app which deals with sign-in, log-in
    path('', include('SignIn.urls')),

    # to the polls app
    path('polls/', include('polls.urls')),
]
