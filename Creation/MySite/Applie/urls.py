from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="Homepage"),
    url(r'^signup$', views.signup, name="signup"),
    url(r'^login$', views.user_login, name="login")
    ]
