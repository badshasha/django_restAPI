from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.drinkList , name='index'),
    path('drink/<int:id>/', views.drinkinfo , name = "info"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
