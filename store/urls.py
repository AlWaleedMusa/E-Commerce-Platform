from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product/<int:product_id>/", views.product_detail, name="product_detail"),
    path("add/", views.add_edit_product, name="add_product"),
    path("edit/<int:product_id>/", views.add_edit_product, name="edit_product"),
    path("delete/<int:product_id>/", views.delete_product, name="delete_product"),
    path("list_products/<str:cat_slug>/", views.list_products, name="list_products"),
]
