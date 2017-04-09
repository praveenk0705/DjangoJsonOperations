__author__ = 'Praveen'
from django.conf.urls import url
from displayDriver import views



urlpatterns = [
   #url(r'^$', views.DisplayView.as_view()),
    url(r'^$', views.DisplayView, name= 'DisplayView'),
	url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^canvas/$', views.Canvas, name = 'CanvasJS'),

]

