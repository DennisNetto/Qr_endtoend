from django.urls import path
from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("createqr/", views.createqr, name="create"),
    path("create1/", views.create1, name="create1"),

]
