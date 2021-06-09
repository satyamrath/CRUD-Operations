from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("create/", views.create, name="Create"),
    path("search/", views.search, name="Search"),
    path("delete/<int:document_id>", views.delete, name="Delete"),
    path("update/<int:document_id>", views.update, name="Update")
]
