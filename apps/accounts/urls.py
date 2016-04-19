from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^login/oauth/github/$', views.GitHubOauth2CallbackView.as_view(), name='github-oauth2-callback'),
]
