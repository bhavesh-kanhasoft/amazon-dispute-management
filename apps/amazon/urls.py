from django.urls import path
from .views import (
    OrderListView,
    dispute_create,
    dispute_delete,
    dispute_list,
    dispute_update,
)

urlpatterns = [
    path("", OrderListView.as_view(), name="order_list"),
    path("disputes/", dispute_list, name="dispute_list"),
    path("disputes/create/", dispute_create, name="dispute_create"),
    path("disputes/<int:pk>/update/", dispute_update, name="dispute_update"),
    path("disputes/<int:pk>/delete/", dispute_delete, name="dispute_delete"),
]
