from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tasks/$', views.todo_list, name='tasks'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^adding/$', views.adding, name='adding'),
]