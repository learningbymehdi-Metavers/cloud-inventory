from django.urls import path
from .views import export_stock_csv

urlpatterns = [
    path("export/", export_stock_csv, name="export_stock_csv"),
]
