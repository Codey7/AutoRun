from django.conf.urls import url

from AutoRun import views

urlpatterns = [
    url(r'show_users$', views.show_user),
]