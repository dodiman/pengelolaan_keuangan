from django.urls import path
from . import views

app_name = "catatan"

urlpatterns = [
    path("create/", views.catatan_create, name="create"),
    path("<str:pk>/edit/", views.catatan_update, name="update"),
    path("<str:pk>/delete/", views.catatan_delete, name="delete"),
    path("<str:pk>/", views.catatan_detail, name="detail"),
    path("", views.catatan_list, name="list"),
]