from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$',views.new_plot,name='new_plot')]
