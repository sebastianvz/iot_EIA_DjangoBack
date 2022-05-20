from django.urls import path
from . import views

urlpatterns=[path('create_machine/',views.Create_machine.as_view(),name="create_machine"),
  path('create_dots/',views.Create_dots.as_view(),name="create_dots"),
  path('get_dots/<int:codigo>/',views.Get_dots.as_view(),name="get_dots")]


