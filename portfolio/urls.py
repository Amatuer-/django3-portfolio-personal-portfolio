from django.urls import path
from portfolio import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home , name='home'),
    path('discover/', views.discover , name='discover'),

]

