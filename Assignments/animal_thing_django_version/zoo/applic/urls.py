from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('map/', views.map, name='map'),
path('zoolist/', views.zoolist.as_view(), name='zoolist'),
path("zoolist/<int:pk>", views.zoodetail.as_view(), name = "zoodetail"),
path("exhibit/<int:pk>", views.exhibit.as_view(), name="exhibit"),
path("animal/<int:pk>", views.animal.as_view(), name="animal"),
path("about", views.about, name="about"),
path("contact", views.contact, name="contact"),
]