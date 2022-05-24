from django.urls import path
from home_app.views import home, about, login

#URLS MAPPED TO THE HOME PAGE URL

urlpatterns = [
    path("", home),
    path("about/about.html", about),
    path("login/login.com", login),

]
